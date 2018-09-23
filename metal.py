from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
	@abstractmethod
	def play(self):
		pass


class Dog(Animal):
	def play(self):
		print('I will bring the branch back to you :)')

class Cat(Animal):
	def play(self):
		print('I will scratch the walls for you :)')

class Kangoroo(Animal):
	pass


dog = Dog()
cat = Cat()
#kangoo = Kangoroo()
animal = Animal()
dog.play()
cat.play()