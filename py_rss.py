from xml.etree import ElementTree as etree
from collections import Counter
from bs4 import BeautifulSoup
import requests

Exceptions = ['a','A']

URLS = [
	"http://www.origo.hu/contentpartner/rss/hircentrum/origo.xml",
]

# "https://index.hu/24ora/rss/"


for url in URLS:
	print("Processing feed from <{}>".format(url))

	data = requests.get(url = url).text

	RSS = etree.fromstring(data)
	item = RSS.findall('channel/item')

	for entry in item:
		print("Found entry: {}".format(entry))
		print(entry.findtext('guid'))

		urldata = requests.get(url = entry.findtext('guid')).text
		Soup = BeautifulSoup(urldata, 'html.parser')

		ParagraphContent = ""

		for paragraph in Soup.find_all('p'):
			ParagraphContent += paragraph.text
		
		for anchor in Soup.find_all('a'):
			ParagraphContent += anchor.text

		Text = Counter([word for word in ParagraphContent.replace('\r\n',' ').split(' ') if word and not word in Exceptions])		

		print(Text.most_common(n = 5))





















