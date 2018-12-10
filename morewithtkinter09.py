from tkinter import *

root=Tk()
root.geometry("300x200+600+250")
root.config(background="#E0FFFF")
root.resizable(False,False)


def userText(event):
    e1.delete(0,END)
    usercheck=True

def passText(event):
    e2.delete(0, END)
    passcheck=True



a=StringVar()
b=StringVar()
usercheck=False
passcheck=False


Label(root,text="User name",bg="#E0FFFF").place(x=20,y=50)
e1= Entry(root,textvariable=a)
e1.place(x=100,y=50)
#e1.insert(0,"Enter username")
e1.bind("<Button>",userText)
