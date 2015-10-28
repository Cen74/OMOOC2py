from Tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

name = StringVar()

def callback():
    name.set( e.get() ) 
    

b = Button(master, text="get", width=10, command=callback)
b.pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(textvariable=name).pack()  #没有master 也可以

mainloop()