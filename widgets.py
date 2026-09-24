from tkinter import *
from datetime import datetime


root = Tk()
root.title('START OF WIDGETS!')
root.geometry('400x400')

lb1 = Label(text= "Hey There! YAY!", fg='white', bg="#2E2CD2", height=1, width=30)


name_lbl = Label(text="Full Name or Name", bg="#C51239")
name_entry = Entry()


def display():
    name = name_entry.get()
    global message
    message = "Welcome To The App! \nToday's date and time is: "
    greet = "Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, str(datetime.now()) + "\n")

text_box = Text(height=3 )

btn = Button(text="Begin", command=display, height=1, bg="#444591",fg='white')

lb1.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
