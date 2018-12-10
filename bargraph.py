from tkinter import *
window = Tk()
step = 50
x,y,x1,y1 = 50,350,100,350
canvas = Canvas(window, width=450,height=450,background = 'yellow')
canvas.pack()
canvas.create_rectangle(x,y,x1,y1,fill = 'white', tags="r1")
canvas.create_line(20,0,20,400, width = '2')
canvas.create_line(0,350,400,350, width = '2')
while True:
    x,y,x1,y1=x,y-step,x1,y1
    canvas.update()
    canvas.after(150)
    canvas.delete("r1")
    canvas.create_rectangle(x,y,x1,y1,fill = 'blue',tags = "r1")
    if y<100:
        break
x2,y2,x3,y3=150,350,200,350
canvas.create_rectangle(x2,y2,x3,y3,fill = 'red', tags="r2")
while True:
    x2,y2,x3,y3=x2,y2-step,x3,y3
    canvas.update()
    canvas.after(200)
    canvas.delete("r2")
    canvas.create_rectangle(x2,y2,x3,y3,fill = 'red',tags = "r2")
    if y2<200:
        break

x4,y4,x5,y5=250,350,300,350
canvas.create_rectangle(x4,y4,x5,y5,fill = 'green', tags="r3")
while True:
    x4,y4,x5,y5=x4,y4-step,x5,y5
    canvas.update()
    canvas.after(200)
    canvas.delete("r3")
    canvas.create_rectangle(x4,y4,x5,y5,fill = 'green',tags = "r3")
    if y4<150:
        break

window.mainloop()
