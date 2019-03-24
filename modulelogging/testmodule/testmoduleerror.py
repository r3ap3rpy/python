import logging

class testmoduleerror(Exception):
	def __init__(self, message):
		self.logger = logging.getLogger('testmodule')
		self.logger.critical(f'Error creating: {message}')

class testmoduleconnectionerror(object):
	def __init__(self, message):
		self.logger = logging.getLogger('testmodule')
		self.logger.critical(f'Connection error creating: {message}')
		