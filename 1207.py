Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> window = TK()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    window = TK()
NameError: name 'TK' is not defined
>>> window = Tk()
>>> canvas = Canvas(window, width = 400, height = 400, background = 'red')
>>> canvas.create_rectangle(10,10,200,200,fill = 'white')
1
>>> windows.mainloop()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    windows.mainloop()
NameError: name 'windows' is not defined
>>> window.mainloop()
>>> canvas.pack()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    canvas.pack()
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 2137, in pack_configure
    + self._options(cnf, kw))
_tkinter.TclError: can't invoke "pack" command: application has been destroyed
>>> window = Tk()
>>> canvas = Canvas(window, width = 400, height = 400, background = 'red')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    canvas = Canvas(window, width = 400, height = 400, background = 'red')
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 2399, in __init__
    Widget.__init__(self, master, 'canvas', cnf, kw)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 2293, in __init__
    (widgetName, self._w) + extra + self._options(cnf))
_tkinter.TclError: can't invoke "canvas" command: application has been destroyed
>>> 
======================== RESTART: G:/pyprg/tkinter.py ========================
Traceback (most recent call last):
  File "G:/pyprg/tkinter.py", line 6, in <module>
    windows.mainloop()
NameError: name 'windows' is not defined
>>> 
======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================
Traceback (most recent call last):
  File "G:/pyprg/tkinter.py", line 5, in <module>
    canvas.create_circle(10,10,200,200,fill = 'green')
AttributeError: 'Canvas' object has no attribute 'create_circle'
>>> 
======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================
Traceback (most recent call last):
  File "G:/pyprg/tkinter.py", line 7, in <module>
    create_arc(50,50,300,300,start = 10, extent = 60, style = 'arc')
NameError: name 'create_arc' is not defined
>>> 
======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

========================= RESTART: G:/pyprg/graph.py =========================

========================= RESTART: G:/pyprg/graph.py =========================

========================= RESTART: G:/pyprg/graph.py =========================

========================= RESTART: G:/pyprg/graph.py =========================

========================= RESTART: G:/pyprg/graph.py =========================

========================= RESTART: G:/pyprg/graph.py =========================
Traceback (most recent call last):
  File "G:/pyprg/graph.py", line 6, in <module>
    while(j<10):
NameError: name 'j' is not defined
>>> 
========================= RESTART: G:/pyprg/graph.py =========================
Traceback (most recent call last):
  File "G:/pyprg/graph.py", line 6, in <module>
    canvas.create_line(x,0,x,400, width = '3')
NameError: name 'x' is not defined
>>> 
========================= RESTART: G:/pyprg/graph.py =========================

========================= RESTART: G:/pyprg/graph.py =========================

========================= RESTART: G:/pyprg/graph.py =========================
Traceback (most recent call last):
  File "G:/pyprg/graph.py", line 10, in <module>
    canvas.create_line(0,y,400,y, width = '3')
NameError: name 'y' is not defined
>>> 
========================= RESTART: G:/pyprg/graph.py =========================

========================= RESTART: G:/pyprg/graph.py =========================

========================= RESTART: G:/pyprg/graph.py =========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================== RESTART: G:/pyprg/tkinter.py ========================

======================= RESTART: G:/pyprg/animation.py =======================

======================= RESTART: G:/pyprg/animation.py =======================

======================= RESTART: G:/pyprg/animation.py =======================

======================= RESTART: G:/pyprg/animation.py =======================

======================= RESTART: G:/pyprg/animation.py =======================

======================= RESTART: G:/pyprg/animation.py =======================

======================= RESTART: G:/pyprg/animation.py =======================

======================= RESTART: G:/pyprg/animation.py =======================

======================= RESTART: G:/pyprg/animation.py =======================

======================== RESTART: G:/pyprg/button.py ========================
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
button clicked
