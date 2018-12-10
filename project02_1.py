import sqlite3
from tkinter import *
conn = sqlite.connect('polygon.db')
window = Tk()
canvas = Canvas(window,width = 400,height=400,background='yellow')
canvas.pack()
conn.execute('''CREATE TABLE COORDS
            (X    INT,
            Y   INT);''')
while(i<4):
    
    def coord(event):
        x0 = event.x
        y0 = event.y
        canvas.create_oval(x0,y0,x0+3,y0+3,fill = 'blue')
        conn.execute("INSERT INTO COORDS(X,Y) VALUES('"+x0+"','"+y0+"')")
        conn.commit()
        canvas.create_line(x0,y0,x0+5,x0+5,width=3)
canvas.bind("<Button-1>",coord1)
    
conn.close()
