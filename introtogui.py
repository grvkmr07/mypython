from tkinter import *
window = Tk()
canvas = Canvas(window, width = 400, height = 400, background = 'red')
canvas.pack()

canvas.create_oval(30,50,280,300,fill = 'yellow')
canvas.create_rectangle(80,80,130,130,fill = 'black')
canvas.create_rectangle(180,80,230,130,fill = 'black')
canvas.create_oval(150,150,300,300,fill = 'green')

window.mainloop()
