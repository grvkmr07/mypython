#leftclick Menu
from tkinter import *

window = Tk()
canvas = Canvas(window,width=300,height=300,background='blue')
canvas.pack()

def addaction():
    canvas.delete("c1")
    canvas.create_oval(p-50,q-50,p+50,q+50,fill="white",tags="c1")
    canvas.update()

oprmenu = Menu(window,tearoff=1)
oprmenu.add_command(label="Add",command=addaction)
oprmenu.add_command(label="Edit",command=addaction)

def popupmenu(event):
    print(event.x_root,":",event.y_root)
    oprmenu.post(event.x_root,event.y_root)
   
canvas.bind("<Button-1>",popupmenu)
