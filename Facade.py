class TravelOrganizer(object):
	def __init__(self):
		print("TravelOrganizer:: Let me arrange the travel for you!")

	def arrangeTravel(self,destination,typeoftravel):
		print("The destination is {}".format(destination))

		self.meansoftransport = Transporter(destination = destination,typeoftravel = typeoftravel)
		self.meansoftransport.bookTravel()

		self.meansofsleeping = Hotelier()
		self.meansofsleeping.bookRoom()
		self.meansofsleeping.arrangeFood()

class Transporter(object):
	def __init__(self, destination ,typeoftravel):
		print("Arraging transport to destination: {} by means: {} ---".format(destination,typeoftravel))
		self.destination = destination
		self.typeoftravel = typeoftravel

	def bookTravel(self):
		if self.typeoftravel == 'owncar':
			print("Nothing to book, the customer uses his/her own car!")
		elif self.typeoftravel == 'plane':
			print("Booking seats for travelling to: {} by PLANE!".format(self.destination))
		elif self.typeoftravel == 'bus':
			print("Booking seats for travelling to: {} by BUS!".format(self.destination))

class Hotelier(object):
	def __init__(self):
		print('Arranging room for customers. ---')

	def roomFree(self):
		print('Checking if there are any rooms left free?')
		return True

	def bookRoom(self):
		if self.roomFree():
			print('Booking room for customer!')

	def arrangeFood(self):
		print('Arranging food for the customers!')

class RoadTripping(object):
	def __init__(self):
		print('Arranging some sightseeing for the customers. ---')

	def arrangeTour(self):
		print('Arranging some fancy places to visit!')

class You(object):
	def __init__(self, name):
		print('Me:: Whohoooooo we are travelling: {}'.format(name))

	def talkToAgent(self):
		print('Me:: Asking agent to arrange this weekend!')
		manager = TravelOrganizer()
		manager.arrangeTravel(destination='Greece',typeoftravel='plane')

	def __del__(self):
		print('Me:: Thank you mister manager for arranging us this beautiful weekend!')

Me = You('Daniel')
Me.talkToAgent()