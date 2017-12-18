# -*- coding: utf-8 -*-

print ("for:")
#计算1-10的整数和
onetoten = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for x in onetoten:
	sum += x
print ('sum 1-10: %d \n' % sum)

#我是小高斯
sum = 0
for x in range(101):
	sum += x
print ('sum rang(101): %d \n' % sum)

print ("while:")
#计算 100 以内所有奇数之和
sum = 0
n = 0
while n < 100:
	sum += n
	n += 2
print (sum,"\n")


print("test:")
#利用循环依次对 list 中的每个名字打印出 Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for x in L:
	print (x)

len = len(L)
n= 0
while n < len:
	print (L[n])
	n += 1