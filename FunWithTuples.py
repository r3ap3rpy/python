from collections import namedtuple
from enum import Enum
from pprint import pprint

Animal = namedtuple('Animal','name age type')

Ursu = Animal(name='Ursu', age = 8, type = 'King Shepherd')
Suki = Animal(name='Suki', age = 4, type = 'King Shepherd')

print(Ursu)
print(Suki)

print(Suki.name)
print(Suki._asdict())

SukiDict = Suki._asdict()

pprint(SukiDict)

SukiDict['name'] = 'Other'

print(SukiDict)

class Windows_OS(Enum):
	Win_2012R2 = 'NT 6.3'
	Win_2012 = 'NT 6.2'
	Win_2008R2 = 'NT 6.1'
	Win_2008 = 'NT 6.0'

OS = namedtuple('Windows','version')

WIN2012R2 = OS(version=Windows_OS.Win_2012R2)
WIN2012 = OS(version=Windows_OS.Win_2012)
WIN2008R2 = OS(version=Windows_OS.Win_2008R2)
WIN2008 = OS(version=Windows_OS.Win_2008)
pprint(WIN2012R2)
pprint(WIN2012)
pprint(WIN2008R2)
pprint(WIN2008)



	
