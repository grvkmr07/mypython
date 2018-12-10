from tkinter import *
window=Tk()
step = 10
x,y,x1,y1 = 100,100,200,200
canvas = Canvas(window,width = 400, height = 400, background = 'red')
canvas.pack()
canvas.create_oval(x,y,x1,y1,fill = 'white',tags = "r1")

while True:
    x,y,x1,y1 = x+step, y-step, x1+step, y1-step
    canvas.update()
    canvas.after(100)
    canvas.delete("r1")
    canvas.create_oval(x,y,x1,y1,fill = 'white',tags = "r1")
    if y1<50:
        x,y,x1,y1 = 100,100,200,200
window.mainloop()
