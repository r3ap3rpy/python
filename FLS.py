class FLS(object):
	def __init__(self, max):
		self._queue = []
		self._max = max

	def __iter__(self):
		for _ in self._queue[::-1]:
			yield _

	def __str__(self):
		return ",".join([str(_) for _ in self._queue[::-1]])

	def push(self, item):
		if len(self._queue) < self._max:
			self._queue.append(item)
		else:
			print("Stack is full, cannot add any new value!")

	def pop(self):
		if len(self._queue) == 0:
			print("Stack is empty, nothing to pop!")
		else:
			self._queue.remove(self._queue[-1])

	def peek(self):
		if len(self._queue) == 0:
			print("Stack is EMPTY!")
			return None
		else:
			return self._queue[-1]

	def isFull(self):
		if len(self._queue) == self._max:
			return True
		else:
			return False
	
	def isEmpty(self):
		if len(self._queue) == 0:
			return True
		else:
			return False
