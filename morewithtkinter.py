#01_Menubar

from tkinter import *

window = Tk()
canvas = Canvas(window,width=300,height=300,background='blue')
canvas.pack()

def line():
    canvas.create_line(20,0,20,400, width = '2')
def oval():
    canvas.create_oval(30,30,60,60, fill = 'yellow')

menubar = Menu(window)
window.config(menu = menubar)




oprmenu = Menu(menubar,tearoff=1)
menubar.add_cascade(label="Operation", menu = oprmenu)


oprmenu.add_command(label="Line",command=line)
oprmenu.add_command(label="Circle",command=oval)

filtermenu = Menu(menubar,tearoff=1)
menubar.add_cascade(label="Filter", menu = filtermenu)

filtermenu.add_command(label="imagefilter",command=oval)
filtermenu.add_command(label="Textfilter",command=oval)

textmenu=Menu(menubar,tearoff=1)
menubar.add_cascade(label="Gourav", menu = textmenu)

textmenu.add_command(label="circle",command=oval)
