#https://rollbar.com/r3ap3rpy/rollbardemo
import rollbar
import os

rollbar.init(os.getenv('ROLL'))

a = int(input('Give me a whole number: '))
b = int(input('Give me a whole number: '))

try:
	c = a / b
	print('The result of a+b = {}'.format(c))
	rollbar.report_message('Calculation is done: a+b = {}'.format(c))
except:
	rollbar.report_exc_info()