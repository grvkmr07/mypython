#ultrasonic data with python

import serial
import re
from tkinter import *


pattern = re.compile(r'[0-9]+')
window = Tk()
canvas = Canvas(window,width=400,height=400,background="white")
canvas.pack()

#canvas.create_rectangle(40,200,80,400,fill="red",tags="bar")
ser = serial.Serial("COM6",9600)

while True:
    s = str(ser.readline())
    d = re.findall(pattern,s)
    x1=50
    y1=110

    if len(d) > 0:
        print(d[0])
        m = int(d[0])
        canvas.delete("bar")
        canvas.delete("data")
        canvas.create_text(200,200,text=d[0],tags="data")
        x1+=m
        y1+=m
        canvas.create_oval(40,100,x1,y1,fill="red",tags="bar")
        canvas.update()
        canvas.after(100)
window.mainloop()

