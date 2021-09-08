# __init__ __repr__
from dataclasses import dataclass

class Animal(object):
    def __init__(self, breed, age, color):
        self._breed = breed
        self._age = age
        self._color = color
    def __repr__(self):
        return f"Dog(breed = {self._breed}, age = {self._age}, color {self._color})"

@dataclass
class DAnimal(object):
    breed: str
    age: int
    color: str

Dog = Animal('German Shepherd',5,'brown')
DDog = DAnimal('Caucasian',3,'grey')
print(Dog)
print(DDog)