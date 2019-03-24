import logging

from .testmoduleerror import testmoduleerror, testmoduleconnectionerror
class testmodule(object):
	def __init__(self):
		self.logger =  logging.getLogger('testmodule')
		self.logger.debug('The init function was called!')

	def error(self, message):
		raise testmoduleerror(f'This is an error: {message}')

	def connection(self, message):
		raise testmoduleconnectionerror(f'This is a connection error: {message}')