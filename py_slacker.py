from slackclient import SlackClient

class NoSlacksForYou(Exception):
	pass

class Slacker(object):
	__token = '<token from slack account>'
	__connection = None
	__channel = ['channelone','channeltwo','general']

	def __init__(self):
		try:
			self.__connection = SlackClient(self.__token)
		except:
			raise NoSlacksForYou('Could not authenticate with this token!')

	def sendMessage(self, channel = 'general', message = None):
		if channel is None:
			raise NoSlacksForYou('You need to specify a valid channel: {}'.format(','.join(self.__channel)))

		if message is None:
			raise NoSlacksForYou('You need to specify a message!')


		try:
			Response = self.__connection.api_call('channel.postMessage',channel = channel, message = message)
		except:
			raise NoSlacksForYou('Could not send this message!')

		return Response

if __name__ == '__message__':
	SCLK = Slacker()
	SCLK.sendMessage(channel = 'Channel to send', message = 'Message to send!')
	SCLK.sendMessage(message = 'Message to send!')









