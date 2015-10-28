# -*- coding: UTF-8 -*-

from Tkinter import *

master = Tk()

e = Entry(master)
e.pack()

# 输入窗口

e.focus_set()

def callback():
    print e.get() #打印输入内容

b = Button(master, text="get", width=10, command=callback())
b.pack()
# 按键会打印输入

mainloop()

e = Entry(master, width=50)
e.pack()
# 重新定义输入窗口

text = e.get()

def makeentry(parent, caption, width=None, **options):
	Label(parent, text=caption).pack(side=LEFT)
	entry = Entry(parent, **options) #定义label和entry
	if width:
		entry.config(width=width)
	entry.pack(side=LEFT)
	return entry
	
user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="10")

content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)
#新的输入窗口

text = content.get()
content.set(text)

