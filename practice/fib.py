# -*- coding: utf-8 -*-
def fib(n,x,y):
	print(y)
	if n == 0:
		return 'end'
	return fib(n-1,y,x+y)
print(fib(10,0,1));


def fib_while(n):
	x,y = 0,1
	while n != 0:
		print(y)
		n=n-1
		x,y = y,x+y
	return 'end'
print(fib_while(10))