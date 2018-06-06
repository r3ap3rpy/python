import asyncio
from time import time

def fibonacci(n):
	return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

async def highest_fibonacci_below(x):
	print(f"Highest fibonacci number below: {x}")
	for y in range(x):
		tmp = fibonacci(y)
		if tmp > x:
			tmp = fibonacci(y - 1)
			print(f"The highest fibonacci number below {x} is {tmp}")
			return tmp
		await asyncio.sleep(0.05)

async def get_results():
	t0 = time()
	await asyncio.wait([
	highest_fibonacci_below(10000),
	highest_fibonacci_below(20000),
	highest_fibonacci_below(1000000),
	highest_fibonacci_below(2000000),
	highest_fibonacci_below(3000000),
	highest_fibonacci_below(30000),
	highest_fibonacci_below(40000),
	highest_fibonacci_below(50000),
	highest_fibonacci_below(60000)
	])
	t1 = time()
	print("This all took me %.2f ms!" % (1000 * (t1 - t0)))

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(get_results())
	loop.close()