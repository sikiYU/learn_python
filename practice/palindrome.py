# -*- coding:utf8 -*-
#回数是指从左向右读和从右向左读都是一样的数，例如 12321， 909。请利用 filter()滤掉非回数
def is_palindrome(n):
	n = str(n)
	n = list(map(int,n))
	#return n == n[::-1] and True or False
	return  n == n[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))