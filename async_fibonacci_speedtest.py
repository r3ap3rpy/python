import asyncio
from time import time
from math import sqrt

def fibo_recursive(n):
	return n if n < 2 else fibo_recursive( n - 1 ) + fibo_recursive( n - 2 )

m = {0:1,1:1}
def fibo_recursive_memoization(n):
	if n not in m:
		m[n] = fibo_recursive_memoization(n - 1) + fibo_recursive_memoization(n - 2)
	return m[n]

def fibo_lucas(n):
	phi = (1 + sqrt(5)) / 2
	return int((phi ** n - (-phi ) ** -n) / sqrt(5))

def fibo_iterative(n):
	i, j = 0, 1
	for k in range(1, n + 1):
		i, j = j, i + j
	return j

async def highest_fibonacci_below(x, function):
	print(f"Highest  fibonacci number below: {x} from function {function.__name__}")
	t0 = time()
	for y in range(x):
		tmp = function(y)
		if tmp > x:
			tmp = function(y - 1)
			print("The highest fibonacci number below %d is %d from function %s, duration %.2f ms!" % (x,tmp,function.__name__,(1000*( time() - t0))))
			return tmp
		await asyncio.sleep(0.05)

async def get_results():
	t0 = time()
	await asyncio.wait([ highest_fibonacci_below(numbahh,function) for numbahh in [10000,20000,1000000,2000000,3000000,30000,40000,50000,6000] for function in [fibo_recursive,fibo_recursive_memoization,fibo_lucas,fibo_iterative]])
	print("This all took me %.2f ms!" % (1000*( time() - t0)))

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(get_results())
	loop.close()