#https://raw.githubusercontent.com/datasets/population-city/master/data/unsd-citypopulation-year-fm.csv

import csv, argparse, os

def coroutine_dec(func):
	def wrap(*args, **kwargs):
		corouted = func(*args,**kwargs)
		corouted.__next__()
		return corouted
	return wrap

@coroutine_dec
def coordinator(writers):
	try:
		while True:
			line = yield
			splitted = line.split(',')
			i = 0
			for writer in writers:
				writer.send(splitted[i])
				i += 1
	except GeneratorExit:
		for writer in writers:
			writer.close()

@coroutine_dec
def file_writer(filename):
	try:
		with open(filename, 'a') as file:
			while True:
				line = yield
				file.write(line + '\n')
	except GeneratorExit:
		file.close()

parser = argparse.ArgumentParser('This tool is to split arbitrary CSV files based on the header into different files with txt extension!')
parser.add_argument('-f','--fileToProcess',type=str,help='Specifies the file to be processed!')
args = parser.parse_args()

if not args.fileToProcess:
	print('You must give me a csv file to process!')
	raise SystemExit

if not os.path.isfile(args.fileToProcess):
	print('You have specified: {} a file which could not be found!'.format(args.fileToProcess))
	raise SystemExit

with open(args.fileToProcess,'r') as csvfile:
	reader = csv.reader(csvfile)
	header = reader.__next__()
	header = [ _.replace(' ','') for _ in header ]

writers = [ file_writer(_+'.txt') for _ in header ]

coordinator = coordinator(writers)

with open(args.fileToProcess,'r') as csvfile:
	for line in csvfile.readlines()[2:]:
		coordinator.send(line)
	coordinator.close()