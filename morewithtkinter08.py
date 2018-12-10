#images
from tkinter import *

window = Tk()

canvas = Canvas(window,width=300,height=300,background="white")
canvas.pack()
x1 = 100
y1=100
d = 10
canvas.create_arc(10,10,x1,y1,start="45",fill="red", width="2",  extent=60, style="pieslice",       tags="circle1")

caImage = PhotoImage(file = "gk.gif")

lb = Label(window,image = caImage )

lb.pack()
window.mainloop()
