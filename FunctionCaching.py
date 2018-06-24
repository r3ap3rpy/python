from functools import lru_cache

@lru_cache(maxsize = 10)
def fibonacci_sequence(n):
	if n < 2:
		return n
	else:
		return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)

print(fibonacci_sequence(10))

fibonacci_sequence.cache_clear()

