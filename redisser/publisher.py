import redis
import sys

if len(sys.argv) == 3:
	program, environment, action = sys.argv

	client = redis.Redis(host = '172.17.39.205', port = 6379)

	client.publish(environment, action)
else:
	print('You must give an environment, and an action!')