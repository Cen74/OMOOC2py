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
        

        #self.label = Label(master, textvariable=self.contents)
        #self.label.pack()

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

