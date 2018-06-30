import requests 

url = "https://www.google.hu/search?q=test+pdf&oq=test+pdf&aqs=chrome..69i57j0l5.3802j0j2&sourceid=chrome&ie=UTF-8"
url = "http://www.orimi.com/pdf-test.pdf"


def download_file(url):
	Result = requests.get(url)	
	with open('Download.pdf','wb') as pdffile:
		pdffile.write(Result.content)

download_file(url)