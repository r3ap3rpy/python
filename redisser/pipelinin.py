import redis

client = redis.Redis(host = "172.18.61.190", port = 6379)

pipline = client.pipeline(transaction = False)
pipline.sadd('mylist','firstelement')
pipline.sadd('mylist','secondelement')
pipline.sadd('mylist','thirdelement')
pipline.sadd('mylist','fourthelement')
pipline.sadd('mylist','fifthelement')
print(pipline.smembers('mylist'))
print(pipline.execute())


with client.pipeline() as mypipe:
	print(mypipe.scard('mylist'))