import xmlrpclib
import requests
import os

class ConfluenceException(Exception):
	pass

class Confluence(object):
	__site = "http://<yourcompany>/confluence"

	def __init__(self, username, password):
		self.__username = username
		self.__password = password
		self.__server = xmlrpclib.ServerProxy(self.__site + "/rpc/xmlrpc")
		self.__token = self.__server.confluence2.login(self.__username,self.__password)
		self.__loginString = "?os_username={}&amp;os_password={}".format(self.__username,self.__password)

	def craftDownloadSpaceUrl(self, spaceName, exportType):
		self.__spaceURL = self.__server.confluence2.exportSpace(self.__token, spaceName, exportType)

	def getSpaceContent(self, location, name):
		if not os.path.isdir(location):
			raise ConfluenceException('The secified location is not visible!')

		HEADER = {'Authorization':'token {}'.format(self.__token)}

		try:
			ZipFile = requests.get(self.__spaceURL + self.__loginString, auth = requests.auth.HTTPBasicAuth(self.__username, self.__password))
		except:
			raise ConfluenceException("Failed to get the file!") from None

		if ZipFile.status_code == 200:
			with open((location + "ExportedSpace.zip"),"wb") as ZippedFile:
				ZippedFile.write(ZipFile.content)
		else:
			raise ConfluenceException("The HTTP request returned status code: {}".format(ZipFile.status_code))
