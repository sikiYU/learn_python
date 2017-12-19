# -*- coding: utf-8 -*-

#给函数起别名
ysq_abs = abs
print ("abs -10: %d" % ysq_abs(-10))
print ("max is: %d" % max(1,2,3,4))

print ("int('123') %d" % int('123'))
print ("float('12.34') %.2f" % float('12.34'))
print ("str(1.23) %s" % str(1.23))
print ("bool(1) %s" % bool(1))
print ("bool('') %s" % bool(''))

#把一个整数转换成十六进制表示的字符串
print ("hex(255) %s \n" % hex(255))

#定义函数

#自定义一个求绝对值的 my_abs 函数
def my_abs(x):
	if x >= 0:
		return x
	else: 
		return -x

print(my_abs(-10))

#空函数，如果想定义一个什么事也不做的空函数，可以用 pass 语句
def nop():
	pass # pass 可以用来作为占位符

#参数检查 调用函数时，如果参数个数不对， Python 解释器会自动检查出来，并抛出 TypeError
#数据类型检查可以用内置函数 isinstance()实现
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >=0:
		return x
	else:
		return -x
print(my_abs(-100))

#返回多个值,返回一个元祖
#游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
import math

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny
x,y = move(200,300,100,math.pi / 6)
print(x,y)

#请定义一个函数 quadratic(a, b, c)，接收 3 个参数，返回一元二次方程：ax2 + bx + c = 0的两个解 (x=[-b±√(b^2-4ac)]/2a)
def quadratic(a,b,c):
	derta = b * b - 4 * a * c
	if derta < 0:
		return None
	elif derta == 0:
		return -b / (2 * a)
	else:
		x1 = (-b + math.sqrt(derta)) / (2 * a)
		x2 = (-b - math.sqrt(derta)) / (2 * a)
		return x1,x2
print(quadratic(2,3,1))
print(quadratic(1,3,-4))

#函数的参数

##位置参数
#计算 x的n次方 的函数
def power(x,n=1):
	result = x
	while n > 0:
		result = result * n
		n = n - 1
	return result
print(power(2,2))


##默认参数 必须指向不变对象
#wrong -> Python函数在定义的时候,默认参数L的值就被计算出来了,即[],默认参数L也是一个变量,它指向对象[],每次调用该函数,如果改变了L的内容,则下次调用时,默认参数的内容就变了,不再是函数定义时的[]了
def add_param(L=[]):
	L.append('END')
	return L
print(add_param())
print(add_param())
print(add_param(),"\n")

#right -> 修改上面的函数，用 str、None 不变对象来实现
def add_param_v2(L=None):
	if L is None:
		L =[]
	L.append('END')
	return L
print(add_param_v2())
print(add_param_v2(),"\n")


##可变参数 传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个 => tuple
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc(1,2,3))
# *params 表示把 params 这个 list 的所有元素作为可变参数传进去。这种写法相当有用，而且很常见   ???传变量的地址???
params = [2,3,4,5]
print(calc(*params))


##关键字参数 允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 dict ,它可以扩展函数的功能
def fruit(name,price,**des):
	print('name:',name,'price:',price,'des:',des)
fruit('apple',2)
fruit('banana',2,where='hainan',color='yellow')

add_fruit = {'feel':'good'}
fruit('watermelon',4,feel=add_fruit['feel'])
# des 获得的 dict 是 add_fruit 的一份拷贝，对 des 的改动不会影响到函数外的 add_fruit
fruit('watermelon',4,**add_fruit)
print("")


##命名关键字参数 需要一个特殊分隔符*， *后面的参数被视为命名关键字参数,必须传入参数名
def flower(name,price,*,city='beijing',type):
	print(name,price,city,type)
flower('rose','15',type='yueji')
print("")


##参数组合
def f1(a,b,c=0,*args,**kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2,3,'a','b')
f1(1,2,3,'a','b',{'aa':'aaaa'})
f1(1,2,3,'a','b',{'aa':'aaaa'},bbbb='bbbbb')
f2(1,2,d='dddd')
f2(1,2,d=['dddd'],eee='eee')

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
print("")

#要注意定义可变参数和关键字参数的语法：
#*args 是可变参数， args 接收的是一个 tuple；
#**kw 是关键字参数， kw 接收的是一个 dict。
#以及调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入： func(1, 2, 3)，又可以先组装 list 或 tuple，
#再通过*args 传入： func(*(1, 2, 3))；
#过**kw 传入： func(**{'a': 1, 'b': 2})。
#使用*args 和**kw 是 Python 的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#默认值。
#定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数


#递归函数  一个函数在内部调用自身本身
#fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
#尾递归是指，在函数返回的时候，调用自身本身，并且， return 语句不能包含表达式
def fact(n):
	return fact_iter(n,1)

def fact_iter(n,i):
	if n==1:
		return i
	return fact_iter(n-1,n*i)

print(fact(5) , "\n");

#汉诺塔
def move(n,a,b,c):
	if n==1:
		print(a , '-->' , c)
	else:
	    move(n-1,a,c,b)
	    move(1,a,b,c)
	    move(n-1,b,a,c)
move(3,'a','b','c')

#高级特性
#切片
L = list(range(10))
print('slice 0-2: ' , L[0:3])
print('slice 0-2: ' , L[:3])
print('slice 1-2: ' , L[1:3])
print('slice 5-6: ' , L[-2:])
print('slice 5: ' , L[-2:-1])
print('slice 0-6 index 2: ' , L[0:6:2])
print('slice all index 3: ' , L[::3])
print('copy new list' , L[:])
print('slice tuple: ' , (11,22,33,44,55)[:2] , "\n")

#迭代 给定一个 list 或 tuple，我们可以通过 for 循环来遍历这个 list 或tuple，这种遍历我们称为迭代
d={'a':1,'b':2,'c':3,'d':4}
for k in d:
	print(k)
#dict 的存储不是按照 list 的方式顺序排列，所以，迭代出的结果顺序很可能不一样
for v in d.values():
	print(v)

for k,v in d.items():
	print(k ,":" ,v)

#字符串也是可迭代对象
for char in 'ABCD':
	print(char)

#collections模块的Iterable类型判断
from collections import Iterable
print("int can interatle ? " , isinstance(123,Iterable))

#带下标循环
for k,v in enumerate(['A','B','C']):
	print(k,v);

for x,y in [(1,1),(2,2),(3,3)]:
	print(x,y)


#列表生成式
#生成[1x1, 2x2, 3x3, ..., 10x10]
L = [x * x for x in range(1,11)]
print(L)

#偶数的平方
L = [x * x for x in range(1,11) if x % 2 ==0]
print(L)

#两层循环，生成全排列
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

#列出当前目录下的所有文件和目录名
import os # 导入 os 模块
L = [d for d in os.listdir('.')] # os.listdir 可以列出文件和目录
print(L)

#列表生成式也可以使用两个变量来生成list,v必须为str
d={'a':'123','b':'234','c':'345'}
L = [k + '=' + v for k,v in d.items()]
print(L)

#list中所有的字符串变成小写
d = ['A','B','C']
L = [s.lower() for s in d]
print(L)

#修改列表生成式，通过添加 if 语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [v.lower() for v in L1 if isinstance(v,str)]
print(L2)

#生成器 一边循环一边计算的机制，称为生成器： generator
g = (x * x for x in range(10))
print(g)
print(next(g))

for n in g:
	print(n)
print("")

#生成器
#使用 isinstance()判断一个对象是否是 Iterable 对象
print('[] is Iterable:' , isinstance([],Iterable))
#可以被 next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#生成器都是 Iterator 对象，但 list、 dict、 str 虽然是 Iterable，却不是Iterator
from collections import Iterator
print('[] is Iterator:',isinstance([],Iterator))
#把 list、 dict、 str 等 Iterable 变成 Iterator 可以使用 iter()函数
print('iter([]) is Iterator:',isinstance(iter([]),Iterator) ,"\n")

#凡是可作用于 for 循环的对象都是 Iterable 类型；
#凡是可作用于 next()函数的对象都是 Iterator 类型，它们表示一个惰性计算的序列；
#集合数据类型如 list、 dict、 str 等是 Iterable 但不是 Iterator，不过可以通过 iter()函数获得一个 Iterator 对象
def do_iter():
	L = iter([1,3,5,7,9,0])
	while True:
		try:
			print(next(L))
		except StopIteration:
			break
do_iter()

#高阶函数 把函数作为参数传入
def add(x,y,f):
	return f(x) + f(y)
print('高阶函数:',add(-5,-5,abs))