#creating and resizing of shapes
#leftclick Menu
from tkinter import *
width1=100
width = 10
height = 10
height1=100
window = Tk()
canvas = Canvas(window,width=300,height=300,background='blue')
canvas.pack()
p,q,p1,q1 =20,20,60,40
x,y,z,w=20,20,50,50
def rectangle():
    canvas.delete("c2")
    canvas.create_rectangle(p,q,p1,q1,fill="white",tags="c2")
    canvas.update()
def oval():
    canvas.delete("c1")
    canvas.create_oval(x,y,z,w,fill="white",tags="c1")
    canvas.update()
oprmenu = Menu(window,tearoff=1)
oprmenu.add_command(label="Rectangle",command=rectangle)
oprmenu.add_command(label="Oval",command=oval)
def keycheck(event):
    global width1,height1,width,height
    #print("keysym? ", event.keysym)
    #print("char? ", event.char)
 
    print("keycode? ", event.keycode)
    if event.keycode==37:
        
        width1=width1-10
        canvas.delete('c1')
        canvas.create_oval(10,10,width1,height1,fill='white',tags='c1')
        canvas.update()
    elif event.keycode==38:
        
        height1=height1-10
        canvas.delete('c1')
        canvas.create_oval(10,10,width1,height1,fill='white',tags='c1')
        canvas.update()
    elif event.keycode==39:
        
        width1=width1+10
        canvas.delete('c1')
        canvas.create_oval(10,10,width1,height1,fill='white',tags='c1')
        canvas.update()
    elif event.keycode==40:
        
        height1=height1+10
        canvas.delete('c1')
        canvas.create_oval(10,10,width1,height1,fill='white',tags='c1')
        canvas.update()
    elif event.keycode==68:
        width = width+10
        width1 = width1+10
        canvas.delete('c1')
        canvas.create_oval(width,height,width1,height1,fill='white',tags='c1')
        canvas.update()
    elif event.keycode==65:
        width = width-10
        width1 = width1-10
        canvas.delete('c1')
        canvas.create_oval(width,height,width1,height1,fill='white',tags='c1')
        canvas.update()
    elif event.keycode==87:
        height = height-10
        height1 = height1-10
        canvas.delete('c1')
        canvas.create_oval(width,height,width1,height1,fill='white',tags='c1')
        canvas.update()
    elif event.keycode==83:
        height = height+10
        height1 = height1+10
        canvas.delete('c1')
        canvas.create_oval(width,height,width1,height1,fill='white',tags='c1')
        canvas.update()
def keycheck(event):
    global width1,height1,width,height
    #print("keysym? ", event.keysym)
    #print("char? ", event.char)
 
    print("keycode? ", event.keycode)
    if event.keycode==37:
        
        width1=width1-10
        canvas.delete('c2')
        canvas.create_rectangle(10,10,width1,height1,fill='white',tags='c2')
        canvas.update()
    elif event.keycode==38:
        
        height1=height1-10
        canvas.delete('c2')
        canvas.create_rectangle(10,10,width1,height1,fill='white',tags='c2')
        canvas.update()
    elif event.keycode==39:
        
        width1=width1+10
        canvas.delete('c2')
        canvas.create_rectangle(10,10,width1,height1,fill='white',tags='c2')
        canvas.update()
    elif event.keycode==40:
        
        height1=height1+10
        canvas.delete('c2')
        canvas.create_rectangle(10,10,width1,height1,fill='white',tags='c2')
        canvas.update()
    elif event.keycode==68:
        width = width+10
        width1 = width1+10
        canvas.delete('c2')
        canvas.create_rectangle(width,height,width1,height1,fill='white',tags='c2')
        canvas.update()
    elif event.keycode==65:
        width = width-10
        width1 = width1-10
        canvas.delete('c2')
        canvas.create_rectangle(width,height,width1,height1,fill='white',tags='c2')
        canvas.update()
    elif event.keycode==87:
        height = height-10
        height1 = height1-10
        canvas.delete('c2')
        canvas.create_rectangle(width,height,width1,height1,fill='white',tags='c2')
        canvas.update()
    elif event.keycode==83:
        height = height+10
        height1 = height1+10
        canvas.delete('c2')
        canvas.create_rectangle(width,height,width1,height1,fill='white',tags='c2')
        canvas.update()


def popupmenu(event):
    print(event.x_root,":",event.y_root)
    oprmenu.post(event.x_root,event.y_root)


canvas.bind("<Button-1>",popupmenu)
canvas.bind("<Key>",keycheck)
canvas.pack()
#canvas1.pack()
canvas.focus_set()
window.mainloop()
