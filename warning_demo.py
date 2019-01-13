import warnings
import requests
import sys
# PYTHONWARNINGS

warnings.filterwarnings('once')
#"default"	print the first occurrence of matching warnings for each location (module + line number) where the warning is issued
#"error"	turn matching warnings into exceptions
#"ignore"	never print matching warnings
#"always"	always print matching warnings
#"module"	print the first occurrence of matching warnings for each module where the warning is issued (regardless of line number)
#"once"	print only the first occurrence of matching warnings, regardless of location

if len(sys.argv) == 2:
	Program, URL = sys.argv
	if 'http://' in URL:
		warnings.warn('The connection is insecure!', category = FutureWarning)

	warnings.warn('The connection is insecure!')
	warnings.warn('The connection is insecure!')
	print('This gets printed!')
	Response = requests.get(url = URL)

else:
	warnings.warn('You need to give me a url as an argument!')
