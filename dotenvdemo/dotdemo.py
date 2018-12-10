import dotenv
import sys
import os

dotenv.load_dotenv()

if len(sys.argv) == 2:
	print('Tier based approarch')
	tier = sys.argv[1]
	print(f"Using config from tier: {tier}")
	if tier.lower() == 'dev':
		user = os.getenv('devuser')
		pwd = os.getenv('devpass')
	elif tier.lower() == 'prod':
		user = os.getenv('produser')
		pwd = os.getenv('prodpass')
	else:
		raise SystemExit('Unknown tier!')

	print(f"Working in tier: {tier}, user: {user}, password: {pwd}")

else:
	print('dryrun')