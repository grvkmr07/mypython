Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a,b=0,1
>>> while b<50
SyntaxError: invalid syntax
>>> a,b=0,1
>>> while b<50:
	print(a):
		
SyntaxError: invalid syntax
>>> a,b=0,1
>>> while b<50:
	print(a)
	a,b=b,a+b

	
0
1
1
2
3
5
8
13
21
>>> stock={"colgate":[10,100],"closeup":[15,250]}
>>> total=0
>>> for n in stock:
	total+=stock[n][0]*stock[n][1]
put(total)
SyntaxError: invalid syntax
>>> put(total)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    put(total)
NameError: name 'put' is not defined
>>> print(total)
0
>>> for n in stock:
	total+=stock[n][0]*stock[n][1]

	
>>> total
4750
>>> while b<50:
	a
	a,b=b,a+b

	
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> Hin= Hello
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    Hin= Hello
NameError: name 'Hello' is not defined
>>> print("Hi HEllo")
Hi HEllo
>>> print("GET LOST")
GET LOST
>>> print("Go to hell")
Go to hell
>>> type(total)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    type(total)
NameError: name 'total' is not defined
>>> 
