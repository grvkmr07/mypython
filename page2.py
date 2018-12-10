
from tkinter import *
window = Tk()
window.title("Student")
window.geometry('500x400+10+10')
window.config(background ="#E1AF0B" )
v = IntVar()

def userText(event):
    e1.delete(0,END)
    usercheck=True

def userText1(event):
    e2.delete(0,END)
    usercheck=True

def userText2(event):
    e3.delete(0,END)
    usercheck=True
    
#induce taking and linking from morewithtkinter04.py
label1 = Label(window,text="""Be Honest while filling the information """, font = "24", justify = CENTER, padx = 20,bg='#E1AF0B')
label2 = Label(window,text="""Student """, pady=170, font = "40", justify = CENTER, padx =200,bg='#E1AF0B', relief = GROOVE)
label1.pack()
label2.pack()

a=StringVar()


b=StringVar()

c=StringVar()

#
label3 = Label(window,text="""Name""",bg="#E1AF0B").place(x=30,y=50)

e1=Entry(window,textvariable=a)
e1.place(x=100,y=50)
e1.insert(0,"Enter your Name")
p=e1.get()

e1.bind("<Button>",userText)

#
label4 = Label(window,text="""Email""",bg="#E1AF0B").place(x=30,y=80)

e2=Entry(window,textvariable=b)
e2.place(x=100,y=80)
e2.insert(0,"username@example.com")
q=e2.get()

e2.bind("<Button>",userText1)
#
label5 = Label(window,text="""Date Of Birth""",bg="#E1AF0B").place(x=30,y=110)

e3=Entry(window,textvariable=c)
e3.place(x=100,y=110)
e3.insert(0,"YYYY,MM,DD")
r=e3.get()

e3.bind("<Button>",userText2)
#
label6 = Label(window,text="""AGE""",bg="#E1AF0B").place(x=200,y=110)

e4.place(x=240,y=110)
from datetime import date
m,n,o=e3.get().split('-')
d=date(m,n,o)
d1=date.today
print(int(d1-d))






window.mainloop

