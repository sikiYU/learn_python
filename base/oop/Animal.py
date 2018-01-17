# -*- coding:utf-8 -*-

class Animal(object):
	def run(self):
		print('Animal is running...')

class RunableMixIn(object):
	"""docstring for Runable"""
	def run(self):
		print("running...")

class FlyableMixIn(object):
	"""docstring for Flyable"""
	def fly(self):
		print("running...")

class Mammal(Animal):
	"""docstring for Mammal"""
	
class Bird(Animal):
	"""docstring for Bird"""

class Dog(Mammal, RunnableMixIn):
	"""docstring for Dog"""
	def run(self):
		print(self)
		print("Dog is running...")
	
class Bat(Mammal, FlyableMixIn):
	"""docstring for Bat"""
	def run(self):
		print("Bat is running...")
	
class Bat(Bird, FlyableMixIn):
	"""docstring for Bat"""

class Ostrich(Bird, RunnableMixIn):
	"""docstring for Ostrich"""
		
		

dog = Dog()
dog.run()

def run_twice(animal):
	animal.run()
run_twice(Cat())