# Web 101
## 需求
- 通过网页访问系统:
  - 每次运行时合理的打印出过往的所有笔记
  - 一次接收输入一行笔记
  - 在服务端保存为文件
- 同时兼容 3w 的 Net 版本的命令行界面进行交互

## 记录
###至2015-11-9 

- 了解Web编程和Frame 
首先应该了解Web和Frame是如何工作的，google 了一下，这篇文章[What is a Web Framework?](http://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)，把web和frame的运作机制说得很清楚
  - all a web application really does is send HTML to browsers
  - The HTTP protocol is based on a request-response model
  - Every message in the HTTP protocol has an associated method (or verb). eg. GET or Post
  - HTTP response code: 200(ok), 204(no content) 
  - Python web frameworks all work the same way: they receive HTTP requests, dispatch code that generates HTML, and creates an HTTP response with that content. Two big issue
    - Routing
    - Templates (dynamically generate HTML)


- 测试小程序
根据官方案例修改了下，实现输入内容后在下一个网页显示

```
@get('/diary')
def welcome():
  return '''
        <form action="/diary" method="post">
            输入: <input name="content" type="text" />
            <input value="确认" type="submit" />
        </form>
    '''
@post('/diary')
def print_input():
  content = request.forms.get('content')
  return "you input is %s" % content

run(host='localhost', port=8088, debug=True,reloader=True)
```

- 问题1
下一步就计划在同一网页上显示输入和输出。最开始想法是输出也要也要有一个输出框。在网页上搜了很多w3的教程也没看到如何设置输出框的。最后在别人提醒下才想到html段落等格式都可以显示内容。

### 2015-11-10

- 根据昨日的提示，完成了一个prit.tpl。完成了在同一页面显示输入和输出

```
<html>
      <body>
            <h1> Cen的日记  </h1>
          <form action="/diary" method="post">
            输入: <input
             name="content" type="text" />
            <input value="确认" type="submit" />
          </form>

          <p> 输入内容 ：</p>
            <tr>
            % if content:
            <td>{{content}}</td>
            % end
            </tr>

        </body>
</html>

```

- 计划实现任务最简单版
前几周的代码函数可以复用，实现逻辑比较简单，但有3个问题还待解决

  - 历史日志是多行字符在网页上没有分行，想到两种方案：
    - html 应该有支持多行显示的语法
    - 用readline函数,一行行读取
  - 每次提交的输入依次显示在网页上
  - 如何做到和命令行兼容

- Mac 下查询端口占用和关闭进程的命令

```
lsof -i:<端口号>
kill -9 <进程ID>

```

### 2015-11-11

- 在w3c上看到html会自动忽略多余的空格，因此修改了原来的函数，用readline()替换
原来的read()。测试时发现如果是历史日志为空返回的是一个字符串，也会被逐行打印。
因此增加了个判定条件。

```
<p> 历史内容 ：</p>
          % if type(content) is list: 
            %   for line in content: 
                <br/> {{line}} <br/>
          %   end
          % else: 
            <br/> {{content}} <br/>

```

- 参考requst的文档，考虑实现命令行界面进行交互。

### 2015-11-12
- 通过命令行界面与网站交互目前知道有两种实现方式
    - 利用 curl 命令与网站传输数据，设定及过滤其的输出, 需要用到subprocess 
    - 利用python丰富的库，模拟登陆网站的行为（算是爬虫的雏形？），可选择的很多。最终从简单性使用 request(网页交互）, beatiful soap（html分析）。
- 过程。了解了原理代码其实很简单，预想一下整个程序的运行过程，逻辑就出来了。中间遇到一些小问题
    + 原来用的是```<br/>```作为换行标志，使用get_text()时抓不到正文内容，返回的都是```<br/>``` 当时想到两种解决方案。
        * 再做一个登陆网页，用get_text() 得道全文
        * 可能是函数语分析的逻辑，案例里是 ``` ‘<li> ** </li>’ ```
尝试了第二种果然顺利解决.
- 总结
    - 正确的google 关键词很重要，尽量精确
    - python 库对文字，html 库的处理很多都转换成了uni 对象，关注相关函数参数，返回值的类型对debug比较有帮助。

- 待完成
- [ ] 用curl 实现命令行交互
- [ ] jinja2 模版
- [ ] bootstrap 
- [ ] 数据库 








