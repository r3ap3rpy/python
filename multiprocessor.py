import requests
import time

from multiprocessing.pool import ThreadPool as WorkerPool

numext = 10

urls = ["http://google.com",
	"https://hu-hu.facebook.com/",
	"http://www.haon.hu/",
	"https://arstechnica.com/"]

print('At start: {}'.format(len(urls)))

for i in range(numext):
	urls.extend(urls)

print('After {} extensions: {}'.format(numext,len(urls)))

def HitURL(url):
	#[url, status_code]
	Status = 'N.A.'
	try:
		res = requests.get(url=url)
		Status = res.status_code
	except:
		pass

	return [url, Status]


def ProcessTask(MyTask = None, MyData = None, Speed=10):
	Task = MyTask
	data = MyData
	NumProc = Speed
	pool = WorkerPool(NumProc)
	start_time = time.time()
	start = 0
	end = NumProc
	FINAL_RESULTS = []
	while end < len(data) + NumProc:
		tmp_start = time.time()
		tmp_result = pool.imap_unordered(Task, data[start:end])
		FINAL_RESULTS.extend(tmp_result)
		start = end
		end += NumProc
		tmp_end = time.time()
		slice_duration = round((tmp_end - tmp_start),2)
		remaining = len(data) - start + NumProc
		print('\nProgress :: Total: {}, remaining: {}, speed: {}, urls in {} seconds, time remaining: {} seconds!'.format(len(data),remaining,NumProc,slice_duration,round((remaining / (slice_duration * NumProc)),2)),end="")

	print('\r\nTotal time elapsed: {}'.format(time.time() - start_time))

### Single demon
start = time.time()
ctr = 0
for i in urls:
	HitURL(i)
	if ctr == 10:
		break
	else:
		ctr += 1
end = time.time()
print('\r\nTotal time elapsed: {}'.format(end - start))

### Multi demo!
ProcessTask(MyTask = HitURL, MyData = urls, Speed = 30)