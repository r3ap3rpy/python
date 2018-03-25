from contextlib import contextmanager
from datetime import datetime

@contextmanager
def CustomLog(*args):
	try:
		myfile = open(*args)
		myfile.write('############### Start Date: {} ###############\n'.format(datetime.now()))
		yield myfile		
	finally:
		myfile.write('############### End Date: {} ###############\n'.format(datetime.now()))
		myfile.close()


with CustomLog('index.txt','a') as customfile:
	customfile.write('THis is going to fail!\n')
	customfile.write('THis is going to fail!\n')
	customfile.write('THis is going to fail!\n')
	customfile.write('THis is going to fail!\n')


class CustomLogger(object):
	def __init__(self, file, mode):
		self.mode = mode
		self.file = file

	def __enter__(self):
		self.openfile = open(self.file,self.mode)
		self.openfile.write('############### Start Date: {} ###############\n'.format(datetime.now()))
		return self.openfile

	def __exit__(self, *args):
		self.openfile.write('############### End Date: {} ###############\n'.format(datetime.now()))
		self.openfile.close()

with CustomLogger('CustomLoggerFromClass.txt','a') as fromclass:
	fromclass.write('This is coming from class!\n')