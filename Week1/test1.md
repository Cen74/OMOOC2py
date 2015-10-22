# Week1 交互101
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

## 第一版代码

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

## 遇到问题

### 输入
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

### 文件打开方式
通过file.open(,a+)模式可以直接创建一个日记文件，每次在文件最后追加内容。最开始设想是每次写入文件、保存、再读取、打印。在思考文件操作时想到有两种方式，一种是先打开文件输入，保存，再重新打开读取；一种是file.seek(0)将文件指针重新定位到开始位置。

seek()函数是在笨方法中关于文件写入和读取操作时学到的。另外需要注意到在windows下如果用'w+'模式打开文件，用write()写入内容后，再调用read()会导致乱码。这是一个大坑，现在对其中的原理还不是很清楚。具体可见[python写文件打开后是乱码](http://segmentfault.com/q/1010000000397712)

### 小结
- 新学函数 
	- str.lower()
	- str.strip()
	- f.seek()
	-  while, if 
- 遗留
	-  没有参考芝麻星的卡片，设计思路不太严谨。
		-  好像不是CLI的标准 
		-  缺乏日志功能
	
