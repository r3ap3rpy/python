import marshal

dictionary = {
	'Name' : 'Daniel',
	'Age' : 28,
	'Weight' : 100.0,
	'Motto' : 'Not sure what Im doing but fine!'
}

with open('dictionary.marhal', 'wb') as dict_dump:
	marshal.dump(dictionary, dict_dump)

data = marshal.dumps(dictionary)

print(repr(data))