import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class NoTeamsForYou(Exception):
	pass

class TeamsAPI(object):
	__mapping = {
		'ChannelName':'ChannelMail@company.domain',
		'AnotherChannelName':'AnotherChannelMail@company.domain',
		'your default channel':'yourdefaultchannelsmail@company.domain'
	}
	__From = '<mail address that specifies the sender>'
	__SmtpNode = 'youmailserver.company.domain'
	__SmtpPort = 25
	__smtp_endpoint = None

	def __init__(self):
		self.__smtp_endpoint = smtplib.SMTP(self.__SmtpNode,self.__SmtpPort)

	def sendMessage(self, channel = 'your default channel', subject = 'your default subject', message = None):
		if message is None:
			raise NoTeamsForYou("No message specified, please try again!")

		if not channel in self.__mapping.keys():
			raise NoTeamsForYou("You have specified an invalid channel!")

		if len(message.split('\n')) > 1:
			MailMessage = '<HTML><BODY>'
			for line in message.slit('\n'):
				MailMessage += "<p>{}</p>".format(line)
			MailMessage = '</BODY></HTML>'
		else:
			MailMessage = '''
			<HTML><BODY>
			<p>%s</p>
			</BODY></HTML>
			''' % (message)

		msg = MIMEMultipart('alternative')
		msg['Subject'] = subject
		msg['From'] = self.__From
		msg['To'] = self.__mapping[channel]
		msg.attach(MIMEText(MailMessage,'html'))
		self.__smtp_endpoint.sendmail(self.__From,self.__mapping[channel],msg.as_string())
		self.__smtp_endpoint.quit()

if __name__ == '__main__':
	TAPI = TeamsAPI()
	TAPI.sendMessage(message = 'Test message to channel')
	TAPI.sendMessage(message = 'Test message to channel',channel = 'your default channel')


















