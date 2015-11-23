#目标 
在上周开发基础上, 完成 极简交互式笔记的  PaaS  版本。需求如下:

- 将上周应用网站发布为公网稳定服务 
    - 可以通过固定域名访问系统:
    - 每次运行时合理的打印出过往的所有笔记
    - 一次接收输入一行笔记
    - 在服务端保存为文件
 
- 同时兼容 3w 的  Net  版本的命令行界面进行交互
 
    - 可以通过本地命令行工具监察/管理网站:
    - 获得当前笔记数量/访问数量等等基础数据
    - 可以获得所有笔记备份的归档下载

## 任务初步分解

- Paas 是一种云服务。可以通过网上的平台进行软件开发。
 
> Platform as a service  ( PaaS ) is a category of  cloud computing services  that provides a  platform  allowing customers to develop, run, and manage  Web applications  without the complexity of building and maintaining the infrastructure typically associated with developing and launching an app.
 
分解
 
- 有哪些paas 平台可利用，优缺点
- 平台运用
    - 基础：sae
    - 管理／分类：kvdb
- 命令行界面交互
    - 工具管理: 访问统计
- 4w 遗留
    - jinjia2
    - bootstrap
    - 数据库
    - ipython
 
### Paas及SAE
 
Paas 类似于在硬件、数据库管理层和软件编写层之间的一个平台接口，使开发者专注于软件逻辑，不用关心硬件部署、存储、备份等更底层的东西。优势就是节省了开发者的时间和精力，前几年云计算很火，但发展不快现在还有些会被iaas替代的争议，但总体应该是未来的趋势。SAE（新浪云）主要面对开发者，国内发展时间最长，对开发者的支持相对最完善。 [ 新浪SAE、阿里云与盛大云 的比较 ]( http://www.lovezbs.com/UPLOAD/?/article/56)
 
### 数据存储与KVDB
 
[how to use python in the web]( https://docs.python.org/2/howto/webservers.html)   提到数据在web server上有3种存储方式：
 
- relational database / use ORM
    - sql,
    - sql lite, split

- text 文件
 
- object oriented database
 
KVDB 这种 key-value 型数据结构好像应该归位第3类，它更符合web 2.0 和大数据背景下海量的离散数据的现状。为了简单本来想在SAE上也用txt存储，但提示web server error，可能是SAE禁止文件写入操作。
 
- KVDB 数据结构

    [*] 分类、收集、管理
    利用key:value 中的key, 将key 设置为 <TAG>:'录入时间'，这样可以区分同一TAG下不同时间的记录。
        - 但如果多客户端同时输入会被覆盖，同时不能区分不同客户端，以后再改进。
    
    [ ] 备份
    暂时未处理，方向
        - kvdb类里好像有相同功能参数
        - SAE storage
 
### 进展
 
#### web 端
web端开发很简单，直接借鉴w4的成果, 原来的函数略作修改。
 
#### CLI 实现
 
- CLI 交互界面
在原网页上通过requests 实现cli 交互感觉很困难，好多细节需处理。想到另开一个'\cli'的网页用来处理与CLI客户端的交互。这样也可以不用处理html，发送与接收都是字符串(有无其它方式？)。总体举得server和client的对标签的设定、管理蛮复杂的，按照mvp原则逐步实现，先验证接收历史消息 > 标签接收 > ...
 
- 问题
    + control character error
    kv的 key值不能含有空格。直接在python编译器里尝试效率最高
 
    + 如何判断kv里没有数据，几种思路
        * kv class 里有相关函数/属性 - help 没有查到
        * google - 与null 比较，貌似也不对
        * getkeys_by_prefix[''] 实验了下如果没有prefix其实就是所有的keys - ok
 
    + 客户端/服务器交互
    在CLI下如何处理标签花了很多时间。为了偷懒，把cli的各种操作都在服务器URL上有单独页面处理。时间主要花在是处理各种报错上，有很多值得总结的地方，可惜当初对问题记录不及时。经验主要是，出错时尽量多的打印过程、在函数返回值里面有执行结果的反馈。

- 总结

review了小赖同学的代码，很值得学习。

- KVDB 的数据结构设置。提起考虑了很多统计功能，有计数器。
  前期思考时没有考虑清楚, 想走捷径
- 列表推导式、beautifulsoap 的使用
  有很多细节，前面只想尽快完成任务，实际上并没有掌握。因此在新的任务下，回潜意识的排斥用。
 
 

 
 
 
 
 
 

 


 
 
 
 
 
 
 
 
 
 
 
 
 
 