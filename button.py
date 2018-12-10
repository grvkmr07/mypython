from tkinter import *
window = Tk()
step = 10
x,y,x1,y1 = 100,100,200,200
canvas = Canvas(window,width = 400, height = 400, background = 'red')
canvas.pack()
def btnaction():
    print("button clicked")

btn = Button(text="clickme", command = btnaction)
btn.pack()
window.mainloop()
