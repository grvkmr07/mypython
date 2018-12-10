#02_Button Click
from tkinter import *

def btnclick():
     lb.configure(text=ent.get())

window = Tk()

ent = Entry(window)
ent.pack()
lb= Label(window,text="message")
lb.pack()


btn = Button(window,text="message", fg="red",command=btnclick)
btn.pack()
canvas = Canvas(window,width="300",height=300,background="blue")
canvas.pack()

window.mainloop()
