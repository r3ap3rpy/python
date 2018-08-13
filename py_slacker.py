from slackclient import SlackClient

class SlackError(Exception):
	pass

class Slack(object):
	__token = "<your token comes here>"
	__connection = None
	__channel = ['<channel_one>','<channel_two>']

	def __init__(self):
		try:
			self.__connection = SlackClient(self.__token)
		except:
			raise SlackError("Could not initialize the connection!")

	def postMessage(self, channel = 'our default channel', message = None, showResponse = False):
		if message is None:
			raise SlackError("You need to specify a message!")

		if not channel in self.__channel:
			raise SlackError("You must provide a valid channel, valid channels are: {}".format(','.join(self.__channel)))

		try:
			Response = self.__connection.api_call("chat.postMessage", channel = channel, text = message)
		except:
			raise SlackError("Could not send the message!")

		if showResponse:
			print(Response)

		return Response

if __name__ == '__main__':
	Slacker = Slack()
	Slacker.postMessage(message = "This is my first trial message!")
	Slacker.postMessage(channel = "<The other channel>", message = "The other message!")









