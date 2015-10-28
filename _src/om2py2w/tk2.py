from Tkinter import *

class App:

    def __init__(self, master):
    
        frame = Frame(master)
        frame.pack()
       
        """self.button = Button(
          frame, text="QUIT", fg="red", command=frame.quit
          )
        self.button.pack(side=LEFT)
        
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT) """
        
        self.entrythingy = Entry()
        self.entrythingy.pack(side=LEFT)
        
        self.contents = StringVar()
        
        self.entrythingy["textvariable"] = self.contents
        
        self.entrythingy.bind('<Key-Return>', self.print_contents)
        
    def say_hi(self):
        print "Hi there, everyone!"
        
    def print_contents(self, event):
        print "--->", \
            self.contents.get()
        
root = Tk()

app = App(root)

root.mainloop()
root.destory()
