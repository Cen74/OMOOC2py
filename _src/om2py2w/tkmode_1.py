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

        self.label = Label(master, textvariable=contents)
        self.label.pack()


        #self.entrythingy.bind('<Key-Return>', self.show_input)
        
        
    """def show_input(self, event):
        print "--->", self.contents.get()
        self.label["textvariable"].set(self.contents.get())"""

        
root = Tk()

app = App(root)

root.mainloop()

