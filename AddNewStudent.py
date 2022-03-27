from tkinter import *
import os
import sqlite3 as sql
from PIL import Image,ImageTk

def addNewStudent():
    if USERNAME.get() == '' or NAME.get() == '' or PASSWORD.get() == '':
        lbl_err = Label(error , text="Please enter all the details !" , fg = "red")
        lbl_err.pack()
    else:
        print("Nothing yet ...")




# ======================== Root window ==========================
root=Tk()
root.title("Add New Student ")
root.resizable(width=FALSE, height=FALSE)
root.geometry("%dx%d+%d+%d" %(500,600,500,100))
root.configure(background="#b6effa")

# ========================== Frames of window  =========================
heading = Frame(root , bd=10)
heading.pack(side=TOP , fill = X)
error = Frame(root )
error.pack(side=TOP , fill=X)
details = Frame(root , height = 335 , width = 400)
details.pack(side=TOP , ipady=10 , ipadx = 10, pady=100)

# ========================= Labels =================================
title = Label(heading , text = "Add Details", bg="white", fg="#0a29c4", font=('Helvetica', 48))
title.pack(side=TOP,fill=BOTH,expand=1)

name = Label(details , text="Name " , font=('Helvetica' , 14) , pady = 10 )
name.grid(row=0 , sticky="e")
user = Label(details , text="Username " , font=('Helvetica' , 14) , pady = 10 )
user.grid(row = 1 , sticky="e")
password = Label(details , text="Password " , font=('Helvetica' , 14) , pady = 10 )
password.grid(row = 2 , sticky="e")

# ============================== Variables ===================================
NAME = StringVar()
USERNAME = StringVar()
PASSWORD = StringVar()

# =============================  Values entered from user ====================================
username = Entry(details , text=USERNAME , font = 14 , relief=RIDGE)
username.grid(row = 0 , column = 1)
Pass = Entry(details , text=PASSWORD , show = "*" , font=14 , relief=RIDGE)
Pass.grid(row=1 , column = 1)
Name = Entry(details , text=NAME , font=(14) , relief=RIDGE)
Name.grid(row=2 , column = 1)

# =============================== Buttons =================================================
btn_back = Button(details , text="SUBMIT" , width = 45 )
btn_back.grid(row = 4 , columnspan=2, pady = 25 , padx = 10)


root.mainloop()