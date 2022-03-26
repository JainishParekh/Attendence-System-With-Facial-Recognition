from tkinter import *
import sqlite3 as sql
import os


root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='white')
root.bind("<Escape>", quit)
root.bind("x", quit)


def connectDB():
    global con , c
    con = sql.connect('LogInDataBase.db')
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS `Student` (
        stu_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT )""")
    c.execute("""SELECT * FROM `Student` 
        WHERE `username` = 'Jainish' and `password` = '101'
        """)
    if c.fetchone() is None:
        c.execute("""INSERT INTO `Student` (username , password) 
        VALUES ('Jainish' , '101')
        """)
        c.execute("""INSERT INTO `Student` (username , password) 
        VALUES ('Bhavik' , '085')
        """)
        con.commit()


label = Label(root)
label.pack()


def login(event=None):
    connectDB()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        login_lbl.config(text="Please enter your username and password !" , fg="red")
    else:
        c.execute("SELECT * FROM `Student` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if c.fetchone() is not None:
            # HomeWindow0()
            USERNAME.set("")
            PASSWORD.set("")
            login_lbl.config(text="Logged In" , fg="red")
        else:
            login_lbl.config(text="Invalid username or password", fg="#fa2205")
            USERNAME.set("")
            PASSWORD.set("")   
    c.close()
    con.close()



# ============================== VARIABLES ======================================
USERNAME = StringVar()
PASSWORD = StringVar()

# ============================== FRAMES =========================================
Titel = Frame(root , bd=10,  relief=RIDGE)
Titel.pack(side=TOP, fill=X)
loginHead=Frame(root , height=500, relief=RIDGE)
loginHead.pack(side=TOP, fill=X, ipady=50, ipadx=200)
logIn = Frame(root, height=50, bd=30)
logIn.pack(side=TOP, pady=20)

# ============================= LABELS IN LOG-IN FORM =========================================
title = Label(Titel, text = "Attendence Manageing System", bg="#b6effa", fg="#0a29c4", font=('Helvetica', 64))
title.pack(fill=BOTH,expand=1)

head=Label(loginHead, text= "Log In ", fg="#0a29c4", bg="#b6effa", font=('Verdana',24))
head.pack(fill=BOTH, expand=1)
note=Label(loginHead, text= "*To exit press x", fg="#0a29c4", bg="#b6effa", font=('Verdana',12))
note.pack(fill=BOTH, expand=1)

lbl_username = Label(logIn, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(logIn, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
login_lbl = Label(logIn)
login_lbl.grid(row=2, columnspan=2)

#============================== WIDGETS TO TAKE USER INPUT ==================================
username = Entry(logIn, textvariable=USERNAME, font=(14) , relief=RIDGE)
username.grid(row=0, column=1)
password = Entry(logIn, textvariable=PASSWORD, show="*", font=(14) , relief=RIDGE)
password.grid(row=1, column=1)
#============================== LOG IN BUTTON =================================
login_btn = Button(logIn, text="Log In", width=45, command=login)
login_btn.grid(pady=25, row=3, columnspan=2)
login_btn.bind("<Return>", login)

root.mainloop()