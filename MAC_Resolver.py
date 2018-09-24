import re
import requests
from time import sleep

Patterns = ['^([0-9A-Fa-f]{2}[.|:|-]){5}([0-9A-Fa-f]{2})$','^([0-9A-Fa-f]{4}[.]){2}([0-9A-Fa-f]{4})$','^([0-9A-Fa-f]{12})$']
CompiledPatterns = [ re.compile(_) for _ in Patterns ]

class Resolver(object):
	_endpoint = "https://api.macvendors.com/"
	_allowedSeparators = [' ',',',';']
	def __init__(self):
		try:
			Status = requests.get(url = self._endpoint)
			if Status.status_code != 200:
				raise SystemExit('THe endpoint: {} is unavailable!'.format(self._endpoint))
		except:
			raise SystemExit('THe endpoint: {} is unavailable!'.format(self._endpoint))

	def resolve_macs(self, listofmacs = None, separator = None):
		if isinstance(listofmacs, str):
			if separator is None:
				raise SystemExit('A seprator needs to be specified, valid separators are: <{}>'.format('|'.join(self._allowedSeparators)))
			if not separator in self._allowedSeparators:
				raise SystemExit('The specified separator: {} is invalid, valid separators are: <{}>'.format('|'.join(separator,self._allowedSeparators)))

			MacsToResolve = listofmacs.split(separator)
		elif isinstance(listofmacs, list) or isinstance(listofmacs, set):
			MacsToResolve = listofmacs
		else:
			raise SystemExit('The specified type of element is invalid!')			
		Results = {}
		if len(MacsToResolve) >= 1:
			for mac in set(MacsToResolve):
				if len([ _ for _ in CompiledPatterns if _.match(mac)]) >= 1:
					Result = requests.get(url = (self._endpoint + mac))
					while Result.status_code == 429:
						sleep(1)
						Result = requests.get(url = (self._endpoint + mac))

					if Result.status_code == 200:
						Results[mac] = Result.text
					elif Result.status_code == 404:
						Results[mac] = 'Unknown Vendor'
					else:
						print('Something happened: {}, {}'.format(Result.status_code,Result.text))

				else:
					print('Skipping invalid mac: {}'.format(mac))
			return Results
		else:
			raise SystemExit('You have not specified a valid maclist, aborting!')

if __name__ == '__main__':
	Resolve = Resolver()

	R = Resolve.resolve_macs(listofmacs = '3A-15-20-AD-AB-B1,3E-A9-F4-78-E7-3C,3C-A9-F4-78-E7-3D,F0-1F-AF-4F-B1-D2,3C-A9-F4-78-E7-3C,invalidmac', separator = ',')
	#R = Resolve.resolve_macs(listofmacs = ['3A-15-20-AD-AB-B1','3E-A9-F4-78-E7-3C,3C-A9-F4-78-E7-3D','F0-1F-AF-4F-B1-D2','3C-A9-F4-78-E7-3C','invalidmac'])
	print(R)