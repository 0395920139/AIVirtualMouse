
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir) 
from controller import AIVirtualMouse,AiShowSlide,AIVolume
from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as font
import webbrowser
from view import link_button
# from tkinter import Tk, Frame
class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()
        self.master = Toplevel()
        self.master.title("Migor")
        self.master.resizable(width = False,
                             height = False)
        
        self.master.configure(width = 750, height=400)


        # self.master.iconbitmap('logo.ico')
        self.Window.call('wm', 'iconphoto', self.master._w, PhotoImage(file="./view/img/logoXP.png"))
        # logo = ImageTk.PhotoImage(file = 'logo.ico')
        # sub = logo.subsample(5, 5)
        # master.iconphoto(False, sub)
        image1 = Image.open("./view/img/logo5.png")
        resize_image = image1.resize((400, 400))
        img = ImageTk.PhotoImage(resize_image)
        self.label = Label(self.master, image=img)
        self.label.image = img
        self.label.place(relx=0.05, rely=-0.1)
        self.label = Label(self.master, text="Version 1.0.0", fg='red')
        self.label.place(relx=0.27, rely=0.65)
        buttonFont = font.Font(family='Roboto', size=18)
        buttonFont_menu = font.Font(family='Roboto', size=15)
          
        def Close():
            self.master.destroy()
        self.exit = Button(self.master, text="Exit", font=buttonFont,height = 1, 
          width = 10, relief="groove",command=Close)
        self.exit.place(relx=0.1, rely=0.8)
        self.help = Button(self.master, text="Info", font=buttonFont,height = 1, 
          width = 10, relief="groove",command=self.Help)
        self.help.place(relx=0.4, rely=0.8)
        def callback():
          webbrowser.open_new(r"https://www.youtube.com/watch?v=pecWJAeX1q4")
        self.guide = link_button.Link_Button(self.master, text="Help", action=callback,
                                      font=buttonFont,height = 1, width = 10, relief="groove")
        # self.guide = Button(self.master, text="Guide", font=buttonFont,height = 1, 
        #   width = 10, relief="groove")
        self.guide.place(relx=0.7, rely=0.8)

        self.mouse = Button(self.master, text="Mouse", font=buttonFont_menu,height = 1, 
          width = 15, relief="groove",command=self.Mouse)
        self.mouse.place(relx=0.6, rely=0.15)
        self.slide = Button(self.master, text="Slide", font=buttonFont_menu,height = 1, 
          width = 15, relief="groove",command=self.Slide)
        self.slide.place(relx=0.6, rely=0.35)
        self.volume = Button(self.master, text="Volume", font=buttonFont_menu,height = 1, 
          width = 15, relief="groove",command=self.Volume)
        self.volume.place(relx=0.6, rely=0.55)
        self.master.mainloop()
        

    def Help(self,Help = "Help"):
      self.Helps = Toplevel()
      self.Helps.deiconify()
      self.Helps.title("About Migor Versoin 1.0.0 [Build 122521]")
      self.Helps.iconbitmap("./view/img/logoXP.ico")
      self.Helps.resizable(width = False,
                    height = False)
      self.Helps.configure(width = 470,
                      height = 550,
                      bg = "#C0C0C0")
      self.logoHelps = Image.open("./view/img/logo5.png")
      self.resize_logoHelps = self.logoHelps.resize((100, 100))
      self.logoHelps = ImageTk.PhotoImage(self.resize_logoHelps)
      self.box1 = Label(self.Helps, image= self.logoHelps)
      self.box1.image = self.logoHelps
      self.box1.place(relx=0.05, rely=0.1)
      self.box2 = Label(self.Helps, text="Migor(64 bit) Chương trình Chuột ảo đa năng",bg = "#C0C0C0")
      self.box2.place(relx=0.3, rely=0.12)
      self.box3 = Label(self.Helps, text="Web Site : https://www.facebook.com/Migor28 ",bg = "#C0C0C0")
      self.box3.place(relx=0.3, rely=0.17)
      self.box4 = Label(self.Helps, text="Bản Quyền (C) : 2021 - 2100 Nguyễn Văn Minh ",bg = "#C0C0C0")
      self.box4.place(relx=0.3, rely=0.22)
      self.textInfo = Text(self.Helps,
                             width = 60,
                             height = 19,
                             bg = "#fff",
                             font = "Helvetica 10",
                             padx = 5,
                             pady = 5)
      self.textInfo.place(relx=0.05, rely=0.3)
      text1 = 'Migor Chương trình Chuột ảo đa năng miễn phí.\nMigor chạy trên tất cả các hệ điều hành Windows.\n'
      text2 = "Các thành viên dự án Migor:\n \tNguyễn Văn Minh: Phát triển chính,Quản lý diễn đàn Migor\n\tNguyễn Văn Long: Designer\n\tPhan Hoàng Sơn : Docx"
      text3 = "\nTrang Web của dự án: \n\t https://www.facebook.com/Migor28\nDiễn đàn trợ giúp:\n\thttps://www.facebook.com/Minh.fullstack"
      text4 = "\nLiên lạc:\n\tNguyễn Văn Minh: Giám Đốc\n\tGmail : Minh2k3k4k@gmail.com\n\tPhone : 0328716036\n\tAddress : Công ty cổ phần Migor\n\t(Ngõ 147 Triều Khúc/ Triều Khúc\n\t/ Tân Triều/ Thanh Trì/Hà Nội)"
      message =text1 + text2 + text3 + text4
      self.textInfo.config(state = NORMAL)
      self.textInfo.insert(END,message)
      self.textInfo.config(state = DISABLED)
      self.textInfo.see(END)
    def Mouse(self):
      messagebox.showwarning("Warning", "Please wait 30s")
      try :
        AIVirtualMouse.virtualMouse()
      except :
        messagebox.showerror("Error", "No connect camera")
    def Slide(self):
      messagebox.showwarning("Warning", "Please wait 30s")
      try :
        AiShowSlide.ShowSlide()
      except :
        messagebox.showerror("Error", "No connect camera")
    def Volume(self):
      messagebox.showwarning("Warning", "Please wait 30s")
      try :
        AIVolume.Volume()
      except :
        messagebox.showerror("Error", "No connect camera")


