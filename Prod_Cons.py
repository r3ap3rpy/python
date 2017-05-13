import threading, time, random, queue

class Prod:
	def __init__(self):
		self.product = ['nail','fork','hammer', 'cabbage']
		self.next = 0

	def run(self):
		global q
		while(time.clock() < 10):
			if (self.next < time.clock()):
				f = self.product[random.randrange(len(self.product))]
				g = self.product[random.randrange(len(self.product))]
				q.put(f)
				q.put(g)
				print("Added: {}".format(f))
				self.next += random.random()

class Comnsumer:
	def __init__(self):
		self.next = 0

	def run(self):
		global q
		while(time.clock() < 10):
			print('Queue size: {}'.format(q.qsize()))
			if (self.next < time.clock() and not q.empty()):
				f = q.get()
				print("Remove: {}".format(f))
				self.next += random.random()
			elif q.empty():
				print('Consumer is waiting for product!')

if __name__ == '__main__':
	q = queue.Queue(10)
	p = Prod()
	c = Comnsumer()
	pt = threading.Thread(target=p.run, args = ())
	ct = threading.Thread(target=c.run, args = ())
	pt.start()
	ct.start()
