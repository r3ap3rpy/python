from abc import ABCMeta, abstractmethod

class Transaction(metaclass = ABCMeta):
	@abstractmethod
	def execute(self):
		pass

class SELECT(Transaction):
	def __init__(self, transaction):
		self.trans = transaction

	def execute(self):
		self.trans.SELECT()

class INSERT(Transaction):
	def __init__(self, transaction):
		self.trans = transaction

	def execute(self):
		self.trans.INSERT()

class UPDATE(Transaction):
	def __init__(self, transaction):
		self.trans = transaction

	def execute(self):
		self.trans.UPDATE()

class TransactionManager:
	def SELECT(self):
		print('Performing SELECT operation!')

	def INSERT(self):
		print('Performing INSERT operation!')

	def UPDATE(self):
		print('Performing UPDATE operation!')


class TransactionBroker:
	def __init__(self):
		self.__transactionQeueue = []

	def requestTransaction(self, transaction):
		self.__transactionQeueue.append(transaction)
		transaction.execute()

if __name__ == '__main__':
	traction = TransactionManager()
	tr_select = SELECT(traction)
	tr_insert = INSERT(traction)
	tr_update = UPDATE(traction)

	brkr = TransactionBroker()
	brkr.requestTransaction(tr_select)
	brkr.requestTransaction(tr_insert)
	brkr.requestTransaction(tr_insert)
	brkr.requestTransaction(tr_select)
	brkr.requestTransaction(tr_update)
	brkr.requestTransaction(tr_insert)
	brkr.requestTransaction(tr_update)