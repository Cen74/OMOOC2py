# -*- coding: UTF-8 -*-
from Tkinter import *

class App:

    contents = StringVar()

    def __init__(self, master):
    
        frame = Frame(master)
        frame.pack()
       
        
        self.entrythingy = Entry()
        self.entrythingy.pack()
        

        self.label = Label(master, textvariable=contents)
        self.label.pack()

        self.entrythingy.bind('<Key-Return>', self.show_input)
        
    def show_input(self, event):
        from_input = self.entrythingy.get()
        contents.set(from_input)

        
root = Tk()

app = App(root)

root.mainloop()

