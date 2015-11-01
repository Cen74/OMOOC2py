# Net 101 极简交互式笔记的网络版本

需求如下：
	- 每次运行时合理的打印出过往的所有笔记
	- 一次接收输入一行笔记
	- 在服务端保存为文件:
	   - 在所有访问的客户端可以获得历史笔记
	- 支持多个客户端同时进行笔记记录
   
## 分析
总结上次经验，掌握好节奏，分为以下几步

    - 原型。掌握UDP原理，写出实验模型。
    - 完成日记最小功能逐步实现
        + 消息接收
        + 多端
        + 历史获取

## 进展
> 2015-11-01更新

### sokect 概念
![socket](http://images.cnitblog.com/blog/349217/201312/05225723-2ffa89aad91f46099afa530ef8660b20.jpg)

socket 基础概念很简单，网上随意一搜就找到。这篇文章[简单理解socket](http://www.cnblogs.com/dolphinX/p/3460545.html)讲得比较透。核心就一句话：socket类似于一种文件，在客队端和服务器端各自维护，可以通过写入内容来供对方读取。

### 功能测试
- 首先把python官方文档里最简单的两个例子自己跑了一遍，客户端在执行到connect时报错。一开始没理解是错误原因，当时还算看socket.py里面的228行代码是什么意思，后来在网上案例里看到要把HOST设置为‘localhost'才行，再看错误原因 ‘nodenmae not known’实在太明显了。

``` 
File "socket1_client.py", line 7, in <module>
s.connect((HOST, PORT))
File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py", line 228, in meth
    return getattr(self._sock,name)(*args)
socket.gaierror: [Errno 8] nodename nor servname provided, or not known
```


- 测试这篇[博客](http://blog.csdn.net/hao_ding/article/details/9958007) 里python udp的案例，运行的流程与自己的设想有较大差异。
	- if not sth首先就理解反了，含义是如果sth没有意义（meaningful)。关于if not 还有更深的坑。见stackoverflow上 [why-if-not-better](http://stackoverflow.com/questions/100732/why-is-if-not-someobj-better-than-if-someobj-none-in-python) 
	- accept, recv等socket函数在while里没有一直循环运行，只是在有连接时才会执行到下一步。

