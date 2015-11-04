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

小结
	- 程序与预想不一致的要多打印

> 2015-11-02 更新
### 原型
支持中文，能过接受并返回的udp server 和 client.

server:

```
# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import date
import sys
import os 

HOST = ''
PORT = 4444
BUFSIZ=1024  
ADDR=(HOST,PORT) 

diary_server = socket(AF_INET, SOCK_DGRAM)
diary_server.bind(ADDR)


while True:
	print "waiting for connection"
	(data, addr_client) = diary_server.recvfrom(BUFSIZ)

	content = data.decode('UTF-8')
	print "conncetd from %r, message: %r" % (addr_client, content)

	diary_server.sendto(data, addr_client)
```

client:

```
# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import date
import sys
import os 

HOST = 'localhost'  
PORT = 4444  
BUFSIZ = 1024  
ADDR = (HOST,PORT)  
  
diary_client = socket(AF_INET,SOCK_DGRAM) 

input_c = raw_input(' > ')
data = input_c.decode('UTF-8').encode('UTF-8')

diary_client.sendto(data, ADDR)
(recv, addr) = diary_client.recvfrom(BUFSIZ)

print "recv %r, from %r " % (recv.decode('UTF-8'), addr)

diary_client.close()

```

- 在中文输入上花了不少时间。前面测试那篇博客的代卖，对中文的支持其实是有问题的，让我被误导了很久，充分说明信息源很重要。encode/decode的概念也特别就纠结，在
stack上［'ascii' codec can't decode byte](http://stackoverflow.com/questions/9644099/python-ascii-codec-cant-decode-byte)有案例。
- 体会对基础概念要理解透，细节很重要，很多时候是头脑里没意识到的错误假设影响了你。用’小黄鸭‘把代码解释一遍，有帮助。

###V2 
- 将客户端内容输入到服务器主机上，及时存入日记本。
- 多个客户端同时连入

server:

```

# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import date
import sys
import os 

HOST = ''
PORT = 4444
BUFSIZ=1024  
ADDR=(HOST,PORT) 

diary_server = socket(AF_INET, SOCK_DGRAM)
diary_server.bind(ADDR)

diary = open('diary.txt', 'a+', 0) # 用 with / flush（）也可解决


while True:
    print "waiting for connection"
    (data, addr_client) = diary_server.recvfrom(BUFSIZ)

    content = data.decode('UTF-8')
    print "conncetd from %r, message: %r" % (addr_client, content)
    diary.write(data)
    diary.write('\n')

    
    diary_server.sendto(data, addr_client)

```

client:

```

# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import date
import sys
import os 

HOST = 'localhost'  
PORT = 4444  
BUFSIZ = 1024  
ADDR = (HOST,PORT)  
  
diary_client = socket(AF_INET,SOCK_DGRAM) 


while True:
	input_c = raw_input(' > ')

	if input_c == 'help' or input_c == 'h' or input_c == '?':
		print """press \'q\' or \'quit\' \'bye\' for help
 
press  \'h\' or \'help\' or \'bye\' to exit"""
	elif input_c == 'bye' or input_c == 'q' or input_c == 'quit':
		print "bye"
		break
	else:
		data = input_c.decode('UTF-8').encode('UTF-8')

		diary_client.sendto(data, ADDR)
		(recv, addr) = diary_client.recvfrom(BUFSIZ)

		print "recv %r, from %r " % (recv.decode('UTF-8'), addr)

diary_client.close()

```

### V3

- 客户端登陆时自动打印历史记录
- 通过命令能从服务器获得历史记录

过程比我想象得难多了，各种报错。主要decode,encode 的编码问题。这部分主要在win下面完成的，中文处理上就不同了。

Server:

```
# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import date
import sys
import os 

def diary_history():
    diary = open('diary.txt')
    content = diary.read()
    content = content.decode('UTF-8').encode('UTF-8')  
    diary.close()
    return content #传递unicode的字符串

def foo():
    HOST = ''
    PORT = 4444
    BUFSIZ=1024  
    ADDR=(HOST,PORT) 

    diary_server = socket(AF_INET, SOCK_DGRAM)
    diary_server.bind(ADDR)

    if os.path.exists('diary.txt'):
        file_content = diary_history()
    else:
        file_content = "Empty Diary" 



    diary = open('diary.txt', 'a+', 0) #with statemanet / flush

    while True:
        print "waiting for connection"
        (data, addr_client) = diary_server.recvfrom(BUFSIZ)
        print "conncetd from %r, message: %r" % (addr_client, data)

        if data == 'test': 
            diary_server.sendto(file_content, addr_client)
    
        elif data == 'syn': # 在win power shell 
            #print type(content) 
            diary_server.sendto(diary_history(), addr_client)
        else:
            # print data 如果是中文，传递回来的不能正常显示 
            diary.write(data)
            diary.write('\n')

    diary.close()
    diary_server.close()


if __name__  == '__main__':
    if 1 != len(sys.argv) :
        print ''' Usage: $python main.py '''
    else:
        foo()

```

client:

```
# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import date
import sys
import os 

def foo():

	HOST = 'localhost'  
	PORT = 4444  
	BUFSIZ = 1024  
	ADDR = (HOST,PORT)  
  
	diary_client = socket(AF_INET,SOCK_DGRAM) 
	diary_client.sendto('test', ADDR)
	(feedback, addr) = diary_client.recvfrom(BUFSIZ)
	print addr 
	print feedback.decode('UTF-8')

	while True:
		input_c = raw_input(' > ')

		if input_c == 'help' or input_c == 'h' or input_c == '?':
			print """
			  press \'q\' or \'quit\' \'bye\' for help
 
			  press  \'h\' or \'help\' or \'bye\' to exit

			  press syn to return history"""
		elif input_c == 'bye' or input_c == 'q' or input_c == 'quit':
			print "bye"
			break
		elif input_c == 'syn':
			diary_client.sendto('syn', ADDR)
			history = diary_client.recv(BUFSIZ)
			print history.decode('UTF-8') # utf-8 object
		else:
			data = input_c.decode('gb2312').encode('UTF-8') #windows下中文编码方式为gb2312
			diary_client.sendto(data, ADDR)
			#(recv, addr) = diary_client.recvfrom(BUFSIZ)

			#print "recv: \n %r , from %r " % (recv.decode('UTF-8'), addr)
		
	diary_client.close()

if __name__  == '__main__':
    if 1 != len(sys.argv) :
        print ''' Usage: $python main.py '''
    else:
        foo()

```

遇到问题：

- 对于登陆时显示历史记录，由于对c/s 交互流程不熟悉，想了很久，睡了一觉就想出来了。
- 本来想写在一个函数里，后来尝试分函数写，出现了indent灯一系列错误。
- encode/decode 的概念还是没理解清楚，而且在windows下中文是以gb2312编码，当初用windowns继续写程序时这个坑了我很久。
	- encode 是将一个unicode object 转换成其unicode 编码的字符串，如果不是str的会默认先把对象转化为str
	- decode('code') 是将字符串对应的code（编码方式），转换成unicode object 

小结：

- 计算机是按逻辑运行的，没有解决不了的bug，头脑里假设函数运行的结果，很多时候是对象 type 变化的问题。同时用两个不同系统的电脑有很多坑，编码差异可能有其它更好的解决方案。
- 自己被bug弄得很气馁，解决一个又出现一个，有点着急就陷入到不停的改错中去了。保持冷静，注重细节，保持信心。
- 找到节奏，可以一个番茄时间解决一个问题，只要每天有进步就行。
- 总结遇到的问题多半是由于很多细节不清楚，基础不牢导致的。既要尽快迭代，也需要把核心东西学会了在进行下一步。
- 下一版需要借鉴别人对函数的使用。




