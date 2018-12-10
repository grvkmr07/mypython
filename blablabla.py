from tkinter import *
#from tkinter import Menu
window = Tk()
window.title("Welcome to Profile Setup")
window.geometry('500x400')
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
window.mainloop()
