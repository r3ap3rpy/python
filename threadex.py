import requests
import threading
from queue import Queue
from time import sleep, time

numext = 5
NUM_THRD = 5

urls = ["http://google.com",
	"https://hu-hu.facebook.com/",
	"http://www.haon.hu/",
	"https://arstechnica.com/"]

print('At start: {}'.format(len(urls)))

for i in range(numext):
	urls.extend(urls)

print('After {} extensions: {}'.format(numext,len(urls)))

jobqueue = Queue()
resultqueue = Queue()

class URL_Parser(threading.Thread):
	def __init__(self, jobqueue, resultqueue):
		threading.Thread.__init__(self)
		self.jobqueue = jobqueue
		self.resultqueue = resultqueue

	def run(self):
		while True:
			current_url = self.jobqueue.get()
			uResult = 'N.A.'
			try:
				Result = requests.get(url = current_url)
				uResult = Result.status_code
			except:
				pass

			self.resultqueue.put([current_url, str(uResult)])
			self.resultqueue.task_done()
			self.jobqueue.task_done()

def QueueWatcher(jobq):
	jobq = jobq
	Total = jobq.qsize()
	while not jobq.empty():
		print('\rThere are <<{}>> of <<{}>> remaining!'.format(jobq.qsize(),Total),end="")
		sleep(1)


start = time()

for u in urls:
	jobqueue.put(u)

threading.Thread(target=QueueWatcher, args=(jobqueue,)).start()

for i in range(NUM_THRD):
	t = URL_Parser(jobqueue,resultqueue)
	t.setDaemon(True)
	t.start()

jobqueue.join()

stop = time()

while not resultqueue.empty():
	result = resultqueue.get()
	#print("So this happened: {}".format(','.join(result)))

print("\r\nThis whole took about: {} seconds!".format(round((stop -start),2)))