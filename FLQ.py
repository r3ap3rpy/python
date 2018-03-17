#Comment
class FLQ(object):
	def __init__(self, max):
		self._queue = []
		self._max = max

	def __iter__(self):
		for _ in self._queue:
			yield _

	def __str__(self):
		if len(self._queue):
			return ",".join([str(_) for _ in self._queue])
		else:
			return "EMPTY"

	def __len__(self):
		return len(self._queue)

	def push(self, item):
		if self._max > len(self._queue):
			self._queue.append(item)
		else:
			self._queue.pop(0)
			self._queue.append(item)

	def pop(self, item):
		if len(self._queue):
			try:
				self._queue.index(item)
				self._queue.remove(item)
			except:
				print("The item: {} could not be found!".format(item))
		else:
			print('The Queue is EMPTY!')


