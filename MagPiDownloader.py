import os, sys, requests

#pip install requests

i = 1

while i < 20:
	Path = (os.getenv('HOME') if os.getenv('HOME') else os.getenv('Userprofile'))
	FileName = (('0' + str(i) if i < 10 else str(i)) + '.').join('MagPi.pdf'.split('.'))
	File = os.sep.join([Path, FileName])

	if os.path.isfile(File):
		print("Skipping the download of file: {} as it's already down!".format(FileName))
	else:
		print('Downloading the new magazine: {}'.format(FileName))
		with open(File, 'wb') as f:
			URL = 'https://www.raspberrypi.org/magpi-issues/' + FileName
			try:
				Content = (requests.get(url=URL)).content
				if 'was not found' in str(Content):
					raise Exception
				else:
					f.write(Content)
					print('The magazine: {} was successfully downloaded!'.format(FileName))
			except:
				print('There is nothing more to download!')
				os.remove(File)
	i += 1