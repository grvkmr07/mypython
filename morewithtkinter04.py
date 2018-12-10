#Radio Button
from tkinter import *

root = Tk()

v = IntVar()

def btnclick():
     label1.configure(text="Your option is %i" % v.get())

label1 = Label(root,text="""Choose a programming language:""",   justify = LEFT, padx = 20)

label1.pack()
Radiobutton(root, 
            text="Python",
            padx = 20, 
            variable=v, 
            value=1).pack(anchor=W)
Radiobutton(root, 
            text="Perl",
            padx = 20, 
            variable=v, 
            value=2).pack(anchor=W)



btn = Button(root,text="message", fg="red",command=btnclick)
btn.pack()

mainloop()
