# GUI 101 极简日记桌面版
## 目标
利用Tkinter完成简单日记桌面系统
## 目标分解
大致看了下Tkinter的文档，感觉坑好大，连hello程序理解都很困难。初步想法是：

1. 看官方文档Tourial中class部分，理解基本概念
2. 学习tkinter的基本案例，写出基本交互GUI
3. 结合原来的代码实现基本日记功能
4. 迭代其它：排版、美化等

### 第一版开发
#### 总结
1. 英文文档的难度超出预计，官方文档可能对初学者并不友好，花费的时间太多了。结合tkinter 的案例，自己写出来有利于理解，真正对class灵光一闪的时候是对比了python官方文档和教程里两个不同的案例，一个主要用函数，一个是都放在一个class下实现。
2. 找到必要的知识花费笨功夫学习，难点在于忍受这种不确定性，选择出哪些是必要的知识，进行练习。如果先做笨方法里class相关习题，把这类基础的理解可能会更高效。实际完成作业所需要的代码量很少。
3. 从一个小功能开始写，逐步升级是比较好的方式。自己思考的好处是能想到这些函数、类的创造目的。

#### 代码纪录
- 先实现一个输入窗口，并将输入显示到Label上。这是参考stakcoverflow上的的一个案例。

```
# -*- coding: UTF-8 -*-
from Tkinter import *

class App:
    def __init__(self, master):
    
        frame = Frame(master)
        frame.pack()
       
        
        self.entrythingy = Entry()
        self.entrythingy.pack()
        
        
        contents = StringVar()
        self.entrythingy["textvariable"] = contents

        self.label = Label(master,textvariable=contents)
        self.label.pack()
        
root = Tk()

app = App(root)

root.mainloop()

```
- 用text作为显示，每次回车能把输入框的内容打印出来

```
# -*- coding: UTF-8 -*-
from Tkinter import *

class App:

    def __init__(self, master):
    
        frame = Frame(master)
        frame.pack()
       
        
        self.entrythingy = Entry()
        self.entrythingy.pack()

        self.contents = StringVar()
        self.entrythingy["textvariable"] = self.contents

        self.text = Text(master, height=8, width=60)
        self.text.pack()

        self.entrythingy.bind('<Key-Return>', self.show_input)
        
    def show_input(self, event):
        print " > " , \
            self.entrythingy.get()
        self.text.insert(END, self.contents.get())
        self.text.insert(END, "\n")
        
root = Tk()

app = App(root)

root.mainloop()

```
- 完成日记原型。输入回车后自动清零，输出到text窗口和日记文件。
- 本来考虑通过函数和调用类来完成后台数据的交互，但没想清楚每次回车后的输入怎么传送到这个类外的地方，因此暂时把这些操作写到类里面去。

```
# -*- coding: UTF-8 -*-
from Tkinter import *
import sys
import os 

class App:

    def __init__(self, master):
    
        frame = Frame(master)
        frame.pack()
       
        
        self.entrythingy = Entry()
        self.entrythingy.pack()

        self.contents = StringVar()
        self.entrythingy["textvariable"] = self.contents
       
        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text = Text(master, yscrollcommand=self.scrollbar.set)
        self.text.pack()
        self.scrollbar.config(command=self.text.yview)

        self.print_diary()

        self.entrythingy.bind('<Key-Return>', self.show_input)
        
    def show_input(self, event):
        print " > " , \
            self.entrythingy.get()
        self.text.insert(END, self.contents.get())
        self.text.insert(END, "\n")

        input_f = self.entrythingy.get()

        diary = open('Diary.txt', 'a+')
        diary.write(input_f.encode('utf-8'))
        diary.write("\n")

        self.contents.set("")

    def print_diary(self):
        file_mark = os.path.exists("./Diary.txt")
        if file_mark == True:
            diary = open('Diary.txt', 'r')
            self.text.insert(END, diary.read())
            diary.close()
        else:
            self.text.insert(END, "This is a new diary: \n")
        
        
root = Tk()

app = App(root)


root.mainloop()

```

- 调试中的报错
	- 各种关于instance 没有相关attribute的错误。需要理解class的namespace, obeject基础概念。如：
		
		- AttributeError: App instance has no attribute 'master'
		- TypeError: unbound method __init__#() must be called with Frame instance as first argument (got App instance instead)
		- App instance has no attribute 
	- 另外一个是中文字符串需要转码的问题
		- 'show_input' Non-ASCII character 

#### 遗留
- 后台数据独立交互（可能有相关函数）
- 美观、优化
- class 这种面向对象的编程的思维方式有点奇妙，可以更深入了解下它的好处。

        