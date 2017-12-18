# -*- coding: utf-8 -*-

#list 和 tuple 是 Python 内置的有序集合，一个可变，一个不可变。根据需要来选择使用
#list
print ("list: ")
hate = ['pear']
fruit = [hate,'apple','orange','banana']
print (fruit)

print ("len: %d" % len(fruit))
print ("first is: %s" % fruit[0][0])
print ("the last one is: %s" % fruit[-1])

fruit.append('watermelon');
print ("append watermelon: ",fruit)

fruit.insert(1,'cherry')
print ("insert cherry into list: ",fruit)

fruit.pop()
print ("delete the last one: ",fruit,"\n")

#tuple:一旦初始化就不能修改,用tuple代替list就尽量用tuple,代码更安全
print ("tuple: ")
color = (4,)
color = ('red','green','bule','black')
print (color);

print ("first is: %s \n" % color[0])


#test
print ("test: ")
L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]
# 打印 Apple:
print(L[0][0])
# 打印 Python:
print(L[1][1])
# 打印 Lisa:
print(L[2][2])