# pip install spookyotp
# pip install Image
from spookyotp import (get_random_secret, TOTP, from_uri)

secret = get_random_secret(n_bytes = 10)
totp = TOTP(secret,'Users name','User@Name.com')
totp.save_qr_code('qr.png')

verification = input('Enter the code you see on your device: ')
if totp.compare(verification):
	print('You have successfully authenticated!')
else:
	print('You have failed the authentication!!')