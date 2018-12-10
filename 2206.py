Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import headerfile
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import headerfile
  File "C:\Python\headerfile.py", line 1
    Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
             ^
SyntaxError: invalid syntax
>>> import headerfile.py
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import headerfile.py
  File "C:\Python\headerfile.py", line 1
    Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
             ^
SyntaxError: invalid syntax
>>> import hearderfile:
	
SyntaxError: invalid syntax
>>> import headerfile
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import headerfile
  File "C:\Python\headerfile.py", line 1
    Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
             ^
SyntaxError: invalid syntax
>>> import os
>>> os.getcwd()
'C:\\Python'
>>> 
====================== RESTART: G:\pyprg\headerfile.py ======================
>>> import headerfile
>>> g = headerfile.circle(9)
>>> g
254.57142857142858
>>> 
====================== RESTART: G:\pyprg\headerfile.py ======================
>>> import headerfile
>>> p = headerfile.rectangle(10,9)
>>> p
90
>>> 
========================= RESTART: G:/pyprg/cache.py =========================
p
>>> import os
>>> os.getcwd()
'G:\\pyprg'
>>> 
========================== RESTART: G:/pyprg/sav.py ==========================
>>> import sav
>>> p= sav.cone(2,3)
>>> p
>>> 
========================== RESTART: G:/pyprg/sav.py ==========================
>>> import sav
>>> p= sav.cone(3,4)
>>> p
(264.0, 5.0, 47.142857142857146)
>>> 
========================== RESTART: G:/pyprg/sav.py ==========================
>>> import sav
>>> p = sav.cone(3,4)
>>> p
(264.0, 5.0, 47.142857142857146)
>>> 
========================== RESTART: G:/pyprg/sav.py ==========================
>>> 
========================== RESTART: G:/pyprg/sav.py ==========================
>>> import sav
>>> p=sav.cone(3,4)
>>> p
(264.0, 5.0, 47.142857142857146)
>>> cone._doc_
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    cone._doc_
AttributeError: 'function' object has no attribute '_doc_'
>>> 
========================== RESTART: G:/pyprg/sav.py ==========================
>>> cone._doc_
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    cone._doc_
AttributeError: 'function' object has no attribute '_doc_'
>>> cone.__doc__
'This program contains volume, slant height and surfacearea respectively'
>>> #DATE AND TIME
>>> from datetime import date
>>> d=date.date()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d=date.date()
AttributeError: type object 'datetime.date' has no attribute 'date'
>>> from datetime import date
>>> d= datetime.date()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d= datetime.date()
NameError: name 'datetime' is not defined
>>> from datetime import date
>>> d=date.today()
>>> print()d
SyntaxError: invalid syntax
>>> print(d)
2018-06-22
>>> type(d)
<class 'datetime.date'>
>>> str(d)
'2018-06-22'
>>> print()d

