from tkinter import *
window = Tk()
canvas = Canvas(window, width = 400, height = 400, background = 'white')
canvas.pack()
x=10
y=10
for i in range(50):
    canvas.create_line(x,0,x,400, width = '1')
    x+=15
for i in range(50):
    canvas.create_line(0,y,400,y, width = '1')
    y+=15
window.mainloop()
