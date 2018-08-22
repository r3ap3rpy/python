#pip install python-twitter
#pip install twitter -> the wrong one
import twitter
import os

CK = os.getenv('CK')
CS = os.getenv('CS')
AK = os.getenv('AK')
AS = os.getenv('AS')

Tweeto = twitter.Api(
	consumer_key = CK,
	consumer_secret = CS,
	access_token_key = AK,
	access_token_secret = AS
	)

Tweeto.PostUpdate("Retweet if you are watching this video!")