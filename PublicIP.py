from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import requests

ActualIP = None
try:
	ActualIP = requests.get(url='http://whatismyip.akamai.com').text
except:
	print('There was an error fetching the site, aborting!')
	raise SystemExit

PrevIP = None
with open('PrevIP.txt','r') as f:
	try:
		PrevIP = f.read().strip()
	except FileNotFoundError:
		NewFile = open('PrevIP.txt','a')
		NewFile.close()

if PrevIP == ActualIP:
	print('Nothing has changed, nothing to do!')
else:
	with open('PrevIP.txt','w') as f:
		f.write(ActualIP)
	HTMLMailBody = """
		<HTML>
		<BODY><h4 align="left">Dear Recipient, <br>Your public IP address has changed, thus the e-mail!<br></h4>
		<H5>Old IP: %s</H5>
		<H5>New IP: %s</H5>
		<H4>Best Wishes,<br>Your automator!</H4>
		</BODY>
		</HTML>
	""" % (PrevIP,ActualIP)
	msg = MIMEMultipart('alternative')
	msg['Subject'] = 'New Public IP: %s' % ActualIP
	msg['From'] = 'yourmailmessage'
	msg['To'] = 'yourrecipient'
	msg.attach(MIMEText(HTMLMailBody,'html'))

	try:
		s = SMTP('smtp.gmail.com','587')
		s.startls()
		s.login('yourmailaddress','yourpassword')
		s.sendmail('youremail','yourrecipient',msg.as_string())
	except:
		print('Unable to send mail!')
		