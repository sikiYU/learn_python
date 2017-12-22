# -*- coding: utf-8 -*-
#素数
def odd():
	n = 1
	while True:
		n = n + 2
		yield n

def check(cur):
	return lambda x : x % cur > 0  

def prime():
	yield 2
	N = odd()
	while True:
		cur = next(N)
		yield cur
		N = filter(check(cur), N)

def print_prime():
	for x in prime():
		if (x > 100):
			return 'end'
		print(x)

print_prime()