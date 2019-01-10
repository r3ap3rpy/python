import redis
from time import sleep

client = redis.Redis(host = '172.17.39.23', port = 6379)

### demo the strings

client.set('language','Python')
print(client.get('language'))

client.set('language','Python', px = 10000)
print(client.get('language'))
print(client.ttl('language'))
sleep(3)
print(client.ttl('language'))


client.set('language','Python')
print(client.expire('language', 10))
print(client.ttl('language'))
sleep(3)
print(client.ttl('language'))

### demo the sets

client.sadd('pythonlist',"value1","value2","value3","value4")
client.sadd('powershelllist',"value4","value5","value6","value7")

print(client.sinter('pythonlist','powershelllist'))
print(client.sunion('pythonlist','powershelllist'))
print(client.scard('pythonlist'))
print(client.scard('powershelllist'))

### demo the hashes

client.hset('Hero','Name','Drow Ranger')
client.hset('Hero','Health','600')
client.hset('Hero','Mana','200')

print(client.hgetall('Hero'))