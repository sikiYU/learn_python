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
#def now():
#	print(datetime.datetime.now().strftime('%Y-%m-%d'))
#要增强 now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改 now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(func):
	def wrapper(*args,**kw):
		print('call %s()' % func.__name__)
		print(args)
		print(kw)
		return func(*args,**kw)
	return wrapper

@log
def now():
	print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
now()
#把@log 放到 now()函数的定义处，相当于执行了语句：now = log(now)
