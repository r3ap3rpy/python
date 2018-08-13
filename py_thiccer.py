import suds
from suds import client
from suds.transport.http import HttpAuthenticated

class NoThyiccForYou(Exception):
	pass

class Thyiccer(object):
	__endpoint = "http://<yourdomain>/webservices/SSWebservice.asmx?wsdl"
	__token = None
	__client = None

	def __init__(self, domain, username, password):
		try:
			self.__client = suds.client.Client(self.__endpoint)
		except:
			raise NoThyiccForYou('Could not reach the endpoint!')

		try:
			self.__token = self.__client.service.Authenticate(username,password,"",domain)
		except:
			raise NoThyiccForYou("The specified credentials were invalid!")


	def getFolders(self):
		try:
			TMP = self.__client.service.SearchFolders(self.__token,"*")
		except:

		try:
			Results = []
			for folder in TMP.Folders.Folder:
				Results.append(folder)
			return Results
		except:
			raise NoThyiccForYou('We could not query the folders')

	def getChildFolders(self, Id):
		try:
			TMP = self.__client.service.FolderGetAllChildren(self.__token, Id)
		except:
			raise NoThyiccForYou('We could not get the child folders!')

		try:
			Results = []
			for folder in TMP.Folders.Folder:
				Results.append(folder)
			return Results
		except:
			raise NoThyiccForYou('We could not get the cild folders!')
	
	def getSecrets(self):
		try:
			TMP = self.__client.service.SearchSecrets(self.__token,"*")
		except:
			raise NoThyiccForYou('We could not get the secrets!')

		try:
			Results = []
			for secret in TMP.SecretSummaries.SecretSummary:
				Results.append(secret)
			return Results
		except:
			raise NoThyiccForYou('We could not get the secrets!')

	def getSecret(self, Id):
		try:
			TMP = self.__client.service.GetSecret(self.__token,Id)
		except:
			raise NoThyiccForYou('We could not get the secret!')

		try:
			Results = []
			for secret in TMP.Secret.Items.SecretItem:
				Results.append(secret)
			return Results
		except:
			raise NoThyiccForYou('We could not get the secrets!')


if __name__ == '__main__':
	THY = Thyiccer(domain = 'mydomain', username = 'myuser', password = 'mypassword')
	print(THY.getSecrets())
	print(THY.getSecret(Id = 182918))
	print(THY.getFolders())
	print(THY.getChildFolders(Id = 101))
	











































