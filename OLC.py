class A(object):
	def __init__(self, animal, age, breed, favourite_toy):
		self.animal = animal
		self.age = age
		self.breed = breed
		self.favourite_toy = favourite_toy

MyDog = A(animal = 'Ursu', age=8, breed = 'King Shephead', favourite_toy = 'the cats')

class B(object):
	def __init__(self, animal, age, breed, favourite_toy):
		self.__dict__.update({ key:value for key, value in locals().items() if key != 'self' })

MyOtherDog = B(animal = 'Szuki', age=4, breed = 'King Shephead', favourite_toy = 'the cats')