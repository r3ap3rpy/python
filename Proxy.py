from random import randint

class Player(object):
	def __init__(self, name):
		self.name = name
		self.price = randint(100000000,900000000)
		self.training = False
		self.vacation = False

	def onTraning(self):
		self.training = True
		return self.training

	def onVacation(self):
		self.vacation = True
		return self.vacation

	def getPrice(self):
		return self.price

	def status(self):
		return (self.vacation or self.training)

class Manager(object):
	def __init__(self, playa):
		self.managed_player = playa
		print('Managing player: {}'.format(self.managed_player.name))


	def send_player_on(self, typeee):
		if typeee in ['vacation','training']:
			if typeee == 'vacation':
				print('Sending player: {} on vacation!'.format(self.managed_player.name))
				self.managed_player.onVacation()
			else:
				print('Sending player: {} on training!'.format(self.managed_player.name))
				self.managed_player.onTraning()
		else:
			print('Cant send player on: {}, it"s not a valid option!'.format(typeee))

	def sell_player(self, offer):
		print('The price of the player is: {}'.format(self.managed_player.getPrice()))
		if offer > self.managed_player.getPrice():
			print('Saying goodbye to: {}'.format(self.managed_player.name))
		else:
			print('Saying NO to offer: {}, as the player is more valuable!'.format(offer))

if __name__ == '__main__':
	fballer = Player('Daniel')
	mgr = Manager(fballer)
	mgr.send_player_on('training')
	mgr.sell_player(72963665812)