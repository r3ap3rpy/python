import requests
from bs4 import BeautifulSoup

URL = "http://www.haon.hu/"

Results = requests.get(url = URL)

if Results.status_code == 200:
	print('Site is read for parsing SIR!')
	PleaseParseItForMe = BeautifulSoup(Results.text,'html.parser')

	print(PleaseParseItForMe.prettify())

	print(PleaseParseItForMe.title)
	print(PleaseParseItForMe.title.name)
	print(PleaseParseItForMe.title.string)
	# <a> </a> 
	for url in PleaseParseItForMe.find_all('a'):
		print(f"Here is your link: {url.get('href')}")

	#print(PleaseParseItForMe.get_text())
else:
	print('I have failed my master!')
