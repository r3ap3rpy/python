import redis

env = 'dev'

client = redis.Redis(host = '172.17.39.205', port = 6379)

p = client.pubsub()
p.subscribe(env)

while True:
	message = p.get_message()

	if message and not message['data'] == 1:
		message = message['data'].decode('utf-8')
		action, platform = message.split('::')
		print(f'Received command: {message}')
		print(f'Action: {action} on platform: {platform}') 
