# Week1 交互101
> 20151027更新，根据大妈演示写了第二版代码
## 任务目标
> - 完成一个极简交互式日记系统,需求如下:
	- 一次接收输入一行日记
	- 保存为本地文件
	- 再次运行系统时,能打印出过往的所有日记

## 任务初步分析
自己目前的程度是做到《笨方法学Python》20题，内容已包含了输入输出、文件的操作，按照大妈的说法结合官方文档应该不难实现。任务可以分解几个部分：

- 创立一个文件存储日记
- 接收输入，并把内容存入到日记文件中
	+ 如何处理一次输入几行和怎么停止输入
- 打印文件内容
	+ 如果用户同意打印日记文件所有内容
- 其它待实现
	+ 日志、记录时间功能
	+ 多用户

## 第一版

```
print "This is Cen's interactive Diary System"

diary = open('Diary.txt', 'a+')

print "I will open the following file: %r" % diary.name


text = ""
stopword = "q"
print "Enter \'q\' to quit input"

while True:
	line = raw_input('input >')
	if line.strip() == stopword:
		break
	text += "%s\n" % line
	
diary.write(text)

diary.seek(0)

print_diary = "If you want to print diary, Enter \'y\'?"
mark = raw_input(print_diary)


if mark.lower() == 'y':
	print "The content of the diary is:"
	print diary.read()
else:
	print "quit the diary"
		
	
diary.close()

```

### 遇到问题

#### 输入
raw_input() 只能一次输入一行，最开始认为python可能有一次输入多行的函数，但在官方文档里没搜索到。想这种需求应该很常见，直接通过google搜索 python input more lines,在stackoverflow上找到[解决方案](http://stackoverflow.com/questions/11664443/raw-input-across-multiple-lines-in-python)。第一答案里面关于iter函数不太理解，先不纠结。选择第二个比较简单的方案，通过设置空白为stopword来控制输入,可以直接使用。str.strip（）函数会删除掉字符串的所有空白，

```
text = ""
stopword = ""
while True:
    line = raw_input()
    if line.strip() == stopword:
        break
    text += "%s\n" % line
print text
```

#### 文件打开方式
通过file.open(,a+)模式可以直接创建一个日记文件，每次在文件最后追加内容。最开始设想是每次写入文件、保存、再读取、打印。在思考文件操作时想到有两种方式，一种是先打开文件输入，保存，再重新打开读取；一种是file.seek(0)将文件指针重新定位到开始位置。

seek()函数是在笨方法中关于文件写入和读取操作时学到的。另外需要注意到在windows下如果用'w+'模式打开文件，用write()写入内容后，再调用read()会导致乱码。这是一个大坑，现在对其中的原理还不是很清楚。具体可见[python写文件打开后是乱码](http://segmentfault.com/q/1010000000397712)

#### 小结
- 新学函数 
	- str.lower()
	- str.strip()
	- f.seek()
	-  while, if 
- 遗留
	-  没有参考芝麻星的卡片，设计思路不太严谨。
		-  好像不是CLI的标准 
		-  缺乏日志功能

## 第二版
分函数，更简洁

```
# -*- coding: utf-8 -*-
from datetime import date
import sys
import os 	
#  根据大妈演示修改

def print_diary():
    file_mark = os.path.exists("./Diary.txt")
    if file_mark == True:
	    print open('Diary.txt').read()
	    
def write_diary():
    diary = open('Diary.txt', 'a+')
    # help = ['help' 'h' '?']
    # quit = ['quit' 'q' 'bye'] 

    while True:
        input = raw_input(' > ')
        if input == 'help' or input == 'h' or input == '?':
            print """press \'q\' or \'quit\' \'bye\' for help
 
press  \'h\' or \'help\' or \'bye\' to exit"""
        elif input == 'bye' or input == 'q' or input == 'quit':
             diary.close()
             print "quit the diary"
             break
        else:
            diary.write(input)
            diary.write('\n')
      
def foo():
    print "This is Cen's interactive Diary System"
    print_diary()    
    write_diary()
       
if __name__  == '__main__':
    if 1 != len(sys.argv) :
        print ''' Usage: $python main.py '''
    else:
        foo()
```
### 遇到问题
#### tab和空格
第一次执行时提示break没有相关的loop, 刚开始以为是语法问题，执行脚本里另外一处类似的命令没有问题，因此排查。后来突然想到以前看到的‘程序员的缩进圣战’，因此想到可能是tab和空格混在一起了，重新敲空格果然问题解决。在python tutorial简要提到了PEP8规范:
> - Use 4-space indentation, and no tabs.
> - Wrap lines so that they don’t exceed 79 characters.
> - Use blank lines to separate functions and classes, and larger blocks of code inside functions.
> - When possible, put comments on a line of their own.
> - Use docstrings.
> - Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
> - Name your classes and functions consistently; the convention is to use CamelCase for classes and lower_case_with_underscores for functions and methods. Always use self as the name for the first method argument 
> - Don’t use fancy encodings if your code is meant to be used in international environments. Plain ASCII works best in any case.

#### while & for in 双循环
最开始设想在 while 输入循环里通过for in 来遍历help等参数，但没想到发现参数后如何打破这两个循环，break 只能结束最近的循环。在stackoverflow上有关于[how to break multiple loops](http://stackoverflow.com/questions/189645/how-to-break-out-of-multiple-loops-in-python)的讨论, 解决方案有三种: 

1. 把内嵌循环放入函数，利用return 打破循环 （推荐，因为flat is better than netsted)
2. 设置两个循环判定变量, 需要break时同时设置为false
3. 利用exception 机制（还未理解）

但对我来说都很复杂。后来发现其实直接使用list功能是最简单的办法：if mark in ['help' '?' 'h']

### 小结
1. 细节与基础很重要。对编程规范和list等常用的操作不熟悉，导致绕了个大弯来解救问题。
2. 专家和普通人的区别之一就是能更快的确定问题的方向，低成本的解决问题。在处理双循环问题上可以不用花那么多时间，直接否定掉这种实现思路，但当时好奇心比较大就是不愿意放弃。在处理问题时要经常想想有哪几种方式，成本效用怎么样，接触多了应该就能更快的选出好的解决方案。
3. 遇到问题尽量去挖，这样才会有收获

### 遗留。
1. 加入时间
2. 日志、多用户功能
