Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> -13/5
-2.6
>>> /13//5
SyntaxError: invalid syntax
>>> -13//5
-3
>>> x = 'True'
>>> y = 'False'
>>> print(x and y==x or y and y==y)
True
>>> y == x
False
>>> x == y
False
>>> u == y
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    u == y
NameError: name 'u' is not defined
>>> y == y
True
>>> print((x and y==x) or (y and y==y))
True
>>> x and y == x
False
>>> y and y==y
True
>>> y == y
True
>>> y
'False'
>>> 5|5
5
>>> 10|5
15
>>> 5|7
7
>>> 5|9
13
>>> 
