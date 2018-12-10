Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list=['orange','apple','banana']
>>> guava in list
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    guava in list
NameError: name 'guava' is not defined
>>> 'guava' in list
False
>>> "orange" in list
True
>>> #FUNCTION
>>> def circle(r):
	area= (22*(r**2))/7
	return area

>>> circle(7)
154.0
>>> 
