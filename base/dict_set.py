# -*- coding: utf-8 -*-
#dict 是用空间来换取时间的一种方法

print ("dict:")
tea = {'green':100,'red':200,'rose':300}
print (tea)
#判断key是否存在
print ('green' in tea)

print ("red price is: %s \n" % tea.get('red'))
print ("juhua price is: %s \n" % tea.get('juhua'))

tea.pop('rose')
print ("delete key: ",tea)

print ("set:")
run = set([6,21,42])
print (run)

run.add(3)
print ("add 3km: ", run)

run.remove(42)
print ("remove longest: ", run)
print ("")

#交集
s1 = set([3,6,9,12,15])
s2 = set([6,12,18])
print ("既是3也是6的倍数：", s1 & s2)
print ("并集：", s1 | s2)


a = 'abc'
b = a.replace('a', 'A')
print (a,b)