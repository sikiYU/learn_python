# -*- coding:utf-8 -*-

class Student(object):
	"""docstring for Student"""
	__slots__='__name','__score'  # 用 tuple 定义允许绑定的属性名称,仅对当前类实例起作用，对继承的子类是不起作用的
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self, name):
		self.__name = name

	def set_score(self, score):
		if not isinstance(score,int):
			raise ValueError('must int')
		if score < 0 or score > 100:
			raise ValueError('1-100')
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

stu1 = Student('Bart','66')
print(stu1.get_score())
stu1.set_score(88)
print(stu1.get_score())
print('DO NOT use bart._Student__name:', stu1._Student__name)


class Student1(object):
	"""docstring for Student1"""
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, score):
		if not isinstance(score,int):
			raise ValueError('must int')
		if score < 0 or score > 100:
			raise ValueError('1-100')
		self._score = score

	@property
	def age(self):
		return 2018

stu1 = Student1()
stu1.score = 99
print(stu1.score)
print(stu1.age)


#请利用@property 给一个 Screen 对象加上 width 和 height 属性，以及一个只读属性 resolution：
import math
class Screen(object):

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self,width):
		self._width = width

	@property
	def height(self):
		return self._width

	@height.setter
	def height(self,height):
		self._height = height

	@property
	def resolution(self):
		return self._width * self._height


# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution