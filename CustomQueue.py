class MyCustomQueue(object):
	def __init__(self, maxlen):
		self._queue = []
		self._maxlen = maxlen

	def push(self, item):
		if len(self._queue) >= self._maxlen:
			self._queue.pop(0)
			self._queue.append(item)
		else:
			self._queue.append(item)

	def __iter__(self):
		for _ in self._queue:
			yield _
	def __len__(self):
		return len(self._queue)

	def __str__(self):
		if len(self._queue) == 0:
			return 'Empty'
		else:
			return ",".join([ str(_) for _ in self._queue ])

