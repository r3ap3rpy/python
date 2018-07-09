from dataclasses import dataclass, asdict, astuple, replace

@dataclass
class Cat:
	name : str
	age : int
	numberOfLegs : int = 4
	numberOfTails : int = 1
	numberOfHead : int = 1
	numberOfEyes : int = 2


print(Cat)

Jack = Cat(name = "Jack", age = 1, numberOfEyes = 1)
Szotyi = Cat(name = "Szotyi", age = 1)

print(Jack)
print(Szotyi)

print(Jack.numberOfEyes)
print(Szotyi.numberOfEyes)

Jack.numberOfEyes = 2

print(Jack.numberOfEyes)

print(asdict(Jack))
print(astuple(Szotyi))
