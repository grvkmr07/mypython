#dot by dot polygon
from tkinter import *
window = Tk()
canvas = Canvas(window,width=400,height=400,background = 'yellow')
canvas.pack()
i=0
x0,y0=0,0
def coord1(event):
    
    x0 = event.x
    y0 = event.y
    #print(x0,y0)
    canvas.create_oval(x0,y0,x0+3,y0+3,fill = 'blue')
 
canvas.bind("<Button-1>",coord1)
    

window.mainloop()

