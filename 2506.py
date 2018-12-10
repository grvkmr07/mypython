Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from datetime import date
>>> d = date.today()
>>> str(d)
'2018-06-25'
>>> d.strftime("%a")
'Mon'
>>> d.strftime("%a-%d")
'Mon-25'
>>> d.strftime("%a-%d%y")
'Mon-2518'
>>> d.strftime("%a-%d-%p-%y")
'Mon-25-AM-18'
>>> d.strftime("%a-%d-%p-%y-%m")
'Mon-25-AM-18-06'
>>> d.strftime("%a-%d-%m-%y-%t")
'Mon-25-06-18-\t'
>>> d.strftime("%a-%d-%m-%y-\%t")
'Mon-25-06-18-\\\t'
>>> d.strftime("%a-%d-%m-%y-%p")
'Mon-25-06-18-AM'
>>> d.strftime("%a-%d-%b-%y-%p")
'Mon-25-Jun-18-AM'
>>> d.strftime("%A-%d-%B-%y-%p")
'Monday-25-June-18-AM'
>>> from datetime import datetime
>>> t = datetime.now()
>>> str(t)
'2018-06-25 13:58:49.535476'
>>> str(t)
'2018-06-25 13:58:49.535476'
>>> from datetime import datetime
>>> t = datetime.now()
>>> str(t)
'2018-06-25 13:59:43.319127'
>>> t.strftime('%H-%M-%S')
'13-59-43'
>>> myname=input()
hi
>>> print(myname)
hi
>>> from datetime import date
>>> d=date(2015,6.4)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d=date(2015,6.4)
TypeError: integer argument expected, got float
>>> d=date(2015,6,4)
>>> d.strftime("%a")
'Thu'
>>> from datetime import date
>>> d = date(1998,12,7)
>>> d.strftime("%a")
'Mon'
>>> #a #A : mon MONTH
>>> #a #A : day DAY
>>> #b #B : mon MONTH
>>> #d    : day
>>> #m    : month in number
>>> #y    : year
>>> #p 	  : AM/PM
>>> #H    : hour in 24hrs format
>>> #I    : hour in 12 hour format
>>> #J    : day of the year
>>> #S    : second
>>> #U    : week in number
>>> # all should be like : %x where 'x' is the alphabetical notation
>>> from datetime import timedelta
>>> 
>>> 

>>> 

>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 

>>> 
>>> #sorry
>>> td = timedelta(days = 100)
>>> d3 = d + + d
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d3 = d + + d
TypeError: bad operand type for unary +: 'datetime.date'
>>> d3 = d + td
>>> d3.strftime("%a-%d-%b-%y")
'Wed-17-Mar-99'
>>> import calender
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
>>> import calendar
>>> calendar.isleap(2026)
False
>>> import calendar
>>> import datetime from date
SyntaxError: invalid syntax
>>> from datetime import date
>>> d = date.today()
>>> d2 = date(2018,8,15)
>>> d2-d
datetime.timedelta(51)
>>> from datetime import date
>>> d = date(2017,12,7)
>>> d1 = date(2018,12,7)
>>> d1-d2
datetime.timedelta(114)
>>> d1-d
datetime.timedelta(365)
>>> #PICKLE AND JASON
>>> import pickle
>>> mlist = [10,12,14,16,18,20]
>>> for open("data.p","Wb")
SyntaxError: invalid syntax
>>> f = open("data.p","Wb")
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    f = open("data.p","Wb")
ValueError: invalid mode: 'Wb'
>>> f = open("data.p","wb")
>>> pickle.dump(mlist,f)
>>> f.close()
>>> 
>>> f = open("data.p","rb")
>>> m = pickle.load(f)
>>> print (m)
[10, 12, 14, 16, 18, 20]
>>> type(m)
<class 'list'>
>>> f.close()
>>> 
>>> import json
>>> d = {'a' : 10, 'b' : 20}
>>> jd = json.dumps(d)
>>> f = open ("d.json" , "w")
>>> f. write(jd)
18
>>> f.close()
>>> 
>>> f = open("d.json")
>>> data = f.read()
>>> f.close()
>>> d2 = json.loads(data)
>>> type(d2)
<class 'dict'>
>>> print(d2)
{'a': 10, 'b': 20}
>>> 
