Python 3.2.3 (default, Oct 19 2012, 19:53:16) 
[GCC 4.7.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> word = 'Help' + 'A'
>>> 
KeyboardInterrupt
>>> word[4]
'A'
>>> word[0:2]
'He'
>>> word[-1]
'A'
>>> word[-1]
'A'
>>> word[-2]
'p'
>>> a = ['spam', 'eggs', 100, 1234]
>>> a
['spam', 'eggs', 100, 1234]
>>> a[0]
'spam'
>>> a[3]
1234
>>> a[1:-1]
['eggs', 100]
>>> a[:2] + ['bacon', 2*2]
['spam', 'eggs', 'bacon', 4]
>>> a[2] = a[2] + 23
>>> a
['spam', 'eggs', 123, 1234]
>>> a[0:2] = [1,12]
>>> a
[1, 12, 123, 1234]
>>> a[0:2] = []
>>> a
[123, 1234]
>>> a[1:1] = ['bletch', 'xyzzy']
>>> a
[123, 'bletch', 'xyzzy', 1234]
>>> a[:0] = a
>>> a
[123, 'bletch', 'xyzzy', 1234, 123, 'bletch', 'xyzzy', 1234]
>>> 
>>> 
>>> len(a)
8
>>> q = [2, 3]
>>> p = [1, q, 4]
>>> len(p)
3
>>> p[1]
[2, 3]
>>> p[1][0]
2
>>> p[1][1]
3
>>> a, b = 0, 1
>>> while b < 10:
...     print(b)
...     a, b = b, a+b
>>> 
>>> a, b = 0, 1
>>> hile b < 10:
	
SyntaxError: invalid syntax
>>> while b < 10:
	print(b)
	a,b - b,a+b

	
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1
(0, 0, 1)
1Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    print(b)
KeyboardInterrupt
>>> a,b=0,1
>>> while b<10:
	print(b)
	a,b = b,a+b

	
1
1
2
3
5
8
>>> 1
1
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...      x = 0
...      print('Negative changed to zero')
... elif x == 0:
...      print('Zero')
... elif x == 1:
...      print('Single')
... else:
...      print('More')
SyntaxError: expected an indented block
>>> 
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...      x = 0
...      print('Negative changed to zero')
... elif x == 0:
...      print('Zero')
... elif x == 1:
...      print('Single')
... else:
...      print('More')
SyntaxError: expected an indented block
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x<0:
	...      x = 0
...      print('Negative changed to zero')
... elif x == 0:
...      print('Zero')
... elif x == 1:
...      print('Single')
... else:
...      print('More')
SyntaxError: invalid syntax
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x<0:
	...      x = 0
...      print('Negative changed to zero')
... elif x == 0:
...      print('Zero')
... elif x == 1:
...      print('Single')
... else:
...      print('More')
SyntaxError: invalid syntax
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x<0:
	x=0;
	print('Negative changed to zero')
    elif x==0:
	    
SyntaxError: unindent does not match any outer indentation level
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x<0:
	x=0;
	print('Negative changed to zero')
elif x==0;
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x<0:
	x=0
	print('Negative changed to zero')
    elif x==0:
	    
SyntaxError: unindent does not match any outer indentation level
>>> x
42
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x<0:
	x = 0
	print('Negative changed to zero')
	elif x==0:
		
SyntaxError: invalid syntax
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x == 42
SyntaxError: invalid syntax
>>> if x == 42:
	print('you got it!')

	
you got it!
>>> if x < 42:
	print('you got it!')

	
>>> if x < 42:
	print('you got it!')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
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


>>> 

>>> 


>>> 
>>> 
>>> 
>>> x = int(input("Please enter an integer: "))
x = int(input("Please enter an integer: "))

Please enter an integer: 42
>>> if x < 0:
	x = 0
	print('Negative')

	
>>> x = int(input("Please enter an integer: "))
x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
	x = 0
	print('Negative')
... elif x == 0:
	
SyntaxError: invalid syntax
>>> x
42
>>> if x == 42:
	print('ok)
	      
SyntaxError: EOL while scanning string literal
>>> if x == 42:
	print('ok')
else:
	print('nope')

	
ok
>>> 
>>> 
>>> x
42

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> if x < 0:
	x = 0
	print('Negative')
elif x ==0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')

	
More
>>> 
