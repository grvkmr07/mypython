from tkinter import *
#from tkinter import Menu
window = Tk()
window.title("Welcome to Profile Setup")
window.geometry('500x400')


def new():    
    
  
    window.title("Category Selection")
    window.geometry('500x400+10+10')
    window.config(background ="#24ECFA" )
    v = IntVar()
    #induce taking and linking from morewithtkinter04.py

    label1 = Label(window,text="""Let know yourself. Punch one of them: """, justify = CENTER, padx = 40,bg='#E0FFFF')
    label1.pack()
    Radiobutton(window, text="Student", padx=30, variable=v,value=1,indicatoron=0, activebackground = 'red',bd='3').pack(anchor=W)
    Radiobutton(window,text="Mentor/Teacher",padx=30,variable=v,value=2,indicatoron=0,activebackground='red',bd='3').pack(anchor=W)
    Radiobutton(window,text="Parents",padx=30,variable=v,value=3,indicatoron=0,activebackground='red',bd='3').pack(anchor=W)

    btn = Button(window,text="Next -->", fg="red",command = 'buttonclick', anchor='center')
    btn.pack()


    
menu = Menu(window)
item = Menu(menu)
item.add_command(label="New",command=new)

menu.add_cascade(label="File", menu=item)
window.config(menu=menu)
window.mainloop()




   
