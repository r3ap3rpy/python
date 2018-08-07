from tqdm import tqdm, trange
from time import sleep

with tqdm(total = 100) as progressbar:
	for i in range(10):
		sleep(0.1)
		progressbar.update(10)


progressbar = tqdm([2,4,6,8,10,12,14,16])

for item in progressbar:
	sleep(0.1)
	progressbar.set_description('Processing element: {}'.format(item))


for i in trange(20):
	sleep(0.1)
	pass


for i in tqdm(range(20)):
	sleep(0.5)
	pass


