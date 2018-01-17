# -*- coding:utf-8 -*-
#返回函数 函数作为返回值 牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量
# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?  书上例子，什么场景能用到呢？
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())

# fix:
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())

#匿名函数
print(list(map(lambda x : x * x ,range(10))))
f = lambda x: x * x
print(f(5))

#装饰器
#函数对象有一个__name__属性，可以拿到函数的名字
print(count.__name__)
print(f1.__name__)

import datetime
import functools
#def now():
#	print(datetime.datetime.now().strftime('%Y-%m-%d'))
#要增强 now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改 now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#自定义log的文本
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print(text, 'call %s()' % func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
now()
print(now.__name__,"\n")
#把@log 放到 now()函数的定义处，相当于执行了语句：now = log(now)
#和两层嵌套的 decorator 相比，3层嵌套的效果是这样的： now = log('execute')(now)
#首先执行 log('execute')，返回的是 decorator函数，再调用返回的函数，参数是 now 函数，返回值最终是 wrapper 函数

#编写一个 decorator，能在函数调用的前后打印出'begin call'和'endcall'的日志
def log_plus(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('begin %s()' % func.__name__)
		func_p = func(*args,**kw)
		print('end %s()' % func.__name__)
		return func_p
	return wrapper
@log_plus
def now_same():
	print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
now_same()

#偏函数 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
#def int2(x, base=2):
#	return int(x, base) 等价于下边的方法
int2 = functools.partial(int,base=2)
kw = {"base": 8}
print(int2('10100',**kw)) #base是几，就传几进制的数

max2 = functools.partial(max,100)
print(max2(*[1,2,34]))