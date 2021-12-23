import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir) 
from tkinter import *
from tkinter import font
from tkinter import ttk
from controller import AIVirtualMouse,AiShowSlide


# imgShow = None
class GUI:
    # constructor method
    def __init__(self):
        # self.imgShow = 
        self.Window = Tk()
        self.Window.withdraw()
        # login window
        self.login = Toplevel()
        # set the title
        self.login.title("Migor")
        self.login.resizable(width = False,
                             height = False)
        self.login.configure(width = 400,
                             height = 300)
        self.mouse = Button(self.login,
                         text = "Mouse",
                         font = "Helvetica 14 bold",
                         command=self.Mouse)
         
        self.mouse.place(relx = 0.1,
                      rely = 0.1)
        self.slideShow = Button(self.login,
                         text = "Slide Show",
                         font = "Helvetica 14 bold",
                         command=self.slideShow)
         
        self.slideShow.place(relx = 0.5,
                      rely = 0.1)
        
        self.Window.mainloop()
 
    def Mouse(self):
        AIVirtualMouse.virtualMouse()
    def slideShow(self):
        AiShowSlide.ShowSlide()
    def receive(self):
        pass
    def sendMessage(self):
        pass
 
# create a GUI class object