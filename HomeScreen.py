import os 
from tkinter import *
from PIL import ImageTk,Image
import pyttsx3

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

text_to_speech('Welcome!')
text_to_speech('Please select from the options..')


def quit(*args):
    root.destroy()


root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='#54d9f7')
root.bind("<Escape>", quit)
root.bind("x", quit)



titel = Label(root,text="Smart Attendence System", bd=20, bg="#c8f7f5", fg="#0a29c4", 
	font=('arial', 64),relief=RIDGE).pack(side=TOP, fill=X)
a = Label(root,text="Welcome to the Facial Recognition", bg="#54d9f7", fg="#0a29c4", 
	font=("arial", 32)).pack()
a=Label(root,text="Attendance System", bg="#54d9f7", fg="#0a29c4", font=("arial", 32)).pack()



add = Image.open("ImagesGUI/AddStudents.png")
add_stu = ImageTk.PhotoImage(add)
add_lbl = Label(root , image=add_stu)
add_lbl.image = add_stu
add_lbl.place(x=180, y=300)

take = Image.open("ImagesGUI/TakingAttendence.png")
takeAtt = ImageTk.PhotoImage(take)
takeAtt_lbl = Label(root , image = takeAtt)
takeAtt_lbl.image = takeAtt
takeAtt_lbl.place(x=615, y=310)

See= Image.open("ImagesGUI/SeeAttendence.png")
SeeAtt = ImageTk.PhotoImage(See)
SeeAtt_lbl = Label(root , image = SeeAtt)
SeeAtt_lbl.image = SeeAtt
SeeAtt_lbl.place(x=980, y=335)

def addNewStudent():
    text_to_speech("Add new student selected ")
    os.system('python AddNewStudent.py')

def TakeAttendence():
    text_to_speech("Take Attendence Selected")
    # os.system('python project.py')


def SeeAttendence():
    text_to_speech("View Attendence selected ")
    # os.system('python ViewAttendence.py')


btn1=Button(root, text="Add a new student data", bd=5, font=('san serief',16),bg="#c8f7f5",fg= "#0a29c4", height=3 , command=addNewStudent).place( x=180, y=570)

btn2=Button(root, text="Take the Attendance", bd=5, font=('times new roman',16),bg="#c8f7f5",fg= "#0a29c4", height=3 , command=TakeAttendence).place( x=625, y=570)

btn3=Button(root, text="View Attendance", bd=5, font=('times new roman',16),bg="#c8f7f5",fg= "#0a29c4", height=3 , command = SeeAttendence).place( x=1050, y=570)

btn4=Button(root, text="EXIT", bd=10, command=quit, font=('times new roman',16),bg="#c8f7f5",fg= "#0a29c4", height=2, width= 10).place( x=645, y=750)


if __name__ == '__main__':
    root.mainloop()