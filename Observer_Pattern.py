
class LadiesAbove30:
	def __init__(self, topic):
		topic.register(self)

	def notify(self, *args, **kwargs):
		print(type(self).__name__,"---> Got", args, "From", topic)


class MenAbove40:
	def __init__(self, topic):
		topic.register(self)

	def notify(self, *args, **kwargs):
		print(type(self).__name__,"---> Got", args, "From", topic)

class Topic:
	def __init__(self):
		self.__clients = []

	def register(self, client):
		self.__clients.append(client)

	def notifyAll(self, *args, **kwargs):
		for client in self.__clients:				
			if kwargs.get('menOnly') and isinstance(client, MenAbove40):
				client.notify(self, *args,**kwargs)
			if kwargs.get('theMoreBeautifulGender') and isinstance(client, LadiesAbove30):
				client.notify(self, *args,**kwargs)

topic = Topic()

Subscribers = []

for i in range(10):
	Subscribers.append(MenAbove40(topic))

for i in range(10):
	Subscribers.append(LadiesAbove30(topic))


topic.notifyAll('Thank you for watching this video, please leave a like and subscribe!', menOnly=True)
topic.notifyAll('Thank you ladies for being awesome!', theMoreBeautifulGender=True)