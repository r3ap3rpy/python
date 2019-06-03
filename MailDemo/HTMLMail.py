import os
import smtplib
import email
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

HTML = """
<!doctype html>
<html>
<body>
<center><H1>This is an HTML mail!</H1></center>
<p>This email has an image and a csv file as attachment!</p>
</body>
</html>
"""

Contacts = ["r3ap3rpy@gmail.com","bountyhunter16@gmail.com"]

msg = MIMEMultipart('mixed')
msg['Subject'] = "An HTML mail with attachments"
msg['To'] = ', '.join(Contacts)
msg['From'] = 'r3ap3rpy@gmail.com'
msg.attach(MIMEText(HTML,'html'))

with open('Test.csv','r') as csv_file:
    att = MIMEApplication(csv_file.read(),_subtype ='csv')
    att.add_header('Content-Disposition','attachment',filename='Test.csv')

msg.attach(att)

with open('Doom.png','rb') as png_file:
    att = MIMEImage(png_file.read(),_subtype='png')
    att.add_header('Content-Disposition','attachment',filename='Doom.png')

msg.attach(att)

sender = smtplib.SMTP_SSL('smtp.gmail.com','465')
sender.ehlo()
sender.login(os.getenv('GUSER'),os.getenv('GPASS'))
sender.sendmail("r3ap3rpy@gmail.com",Contacts,msg.as_string())
sender.close()

