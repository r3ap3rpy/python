class TextReader(object):
	def __init__(self, filename):
		self.filename = filename
		self.file = open(filename)
		self.linenumber = 0

	def readline(self):
		self.linenumber += 1
		line = self.file.readline()
		if not line:
			return None

		if line.endswith('\n'):
			line = line[:-1]
		return "Read line number: {} line: {}".format(self.linenumber, line)

	def __getstate__(self):
		state = self.__dict__.copy()
		del state['file']
		return state

	def __setstate__(self, state):
		self.__dict__.update(state)
		file = open(self.filename)
		for text_line in range(self.linenumber):
			file.readline()

		self.file = file


