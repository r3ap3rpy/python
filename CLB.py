file = open('MyFile.txt','r')
file.read()
file.close()

file = open('MyFile.txt','w')
try:
	file.write('whateveryouwant')
finally:
	file.close()


with open('MyFile.txt','w') as my_file:
	my_file.write('whateverwewant')

import os


class My_Writer(object):
	def __init__(self, name, method):
		with open('Log.txt','a') as audit:
			audit.write('The file = {} for mode = {} was opened by: {}!\n'.format(name,method,os.getenv('USERNAME')))
		self.file = open(name, method)
	def __enter__(self):
		with open('Log.txt','a') as audit:
			audit.write('The handle was returned!\n')
		return self.file
	def __exit__(self, type, value, traceback):
		with open('Log.txt','a') as audit:
			audit.write('The file was closed!\n')
		self.file.close()
