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
        
        #self.label = Label(master, textvariable=self.contents)
        #self.label.pack()

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

