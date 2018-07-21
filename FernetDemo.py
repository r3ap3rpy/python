import os
import cryptography
import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class FernetDemo(object):
	__Content = None
	def __init__(self, File, Key):
		self.File = File
		self.Key = Key.encode('utf-8')
		self.KDF = PBKDF2HMAC(
				algorithm = hashes.SHA256(),
				length = 32,
				salt = 'MyCustomSalt'.encode('utf-8'),
				iterations = 100000,
				backend = default_backend()
			)
		self.encodedKey = base64.urlsafe_b64encode(self.KDF.derive(self.Key))
		self.fern = Fernet(self.encodedKey)

		if not os.path.isfile(self.File):
			with open(self.File,'w') as FileToEncrypt:
				pass

	@property
	def Content(self):
		return self.__Content

	@property
	def FileContent(self):
		with open(self.File,'rb') as DecryptedFile:
			return self.fern.decrypt(DecryptedFile.read()).decode('utf-8')

	def unlockFile(self):
		if not self.__Content is None:
			print("The file is already unlocked!")
			return

		with open(self.File,'rb') as EncryptedFile:
			self.__Content = self.fern.decrypt(EncryptedFile.read()).decode('utf-8')

		print('#Content')
		print(self.__Content)
		print('#Content')

	def addContent(self,ContentToAdd ):
		self.__Content += ContentToAdd
		with open(self.File,"wb") as EncryptedFile:
			EncryptedFile.write(self.fern.encrypt(self.__Content.encode('utf-8')))

	def lockFile(self):
		if self.__Content is None:
			print("There is nothing to add!")
			return

		with open(self.File,"wb") as EncryptedFile:
			EncryptedFile.write(self.fern.encrypt(self.__Content.encode('utf-8')))

FD = FernetDemo(File = 'TestFile.txt',Key='Password123')
FD.unlockFile()
FD.addContent('THis is my first ever encrypted Content!')
FD.addContent('THis is my first ever encrypted Content!')
FD.lockFile()

print(FD.FileContent)

