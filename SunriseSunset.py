import requests, json, datetime, os

def cronner(msg):
	f = open("/var/spool/cron/crontab/<username>","w")
	f.write(msg)
	f.close()

Times = None
try:
	Times = requests.get(url="https://api.sunrise-sunset.org/json?lat=47.4979&lng=19.0402&date=today")
except:
	raise SystemExit

if Times:
	Sunrise = None
	Sunset = None

	try:
		Sunrise = json.loads(Times.text)['results']['sunrise']	
		Sunset = json.loads(Times.text)['results']['sunset']
	except:
		print("Could not parse the json so the execution is aborted!")
		raise SystemExit

	try:
		Sunrise_hour = Sunrise.split(':')[0]
		Sunrise_minute = Sunrise.split(':')[1]
		Sunset_hour = Sunset.split(':')[0]
		Sunset_minute = Sunset.split(':')[1]
	except:
		print("There is something wrong with the format, aborting!")
		raise SystemExit

	msg = 'PATH:/usr/local/bin;/usr/bin:/home/<username>/Scripts/\n'
	msg += '%s %s */1 * * /usr/bin/python /home/<username>/Scripts/Surveillance.py\n' % (Sunrise_minute, Sunrise_hour) 
	msg += '%s %s */1 * * /usr/bin/python /home/<username>/Scripts/KillSurveillance.sh\n' % (Sunset_minute, int(Sunset_hour) + 14)

	try:
		cronner(msg)
		os.system('crontab -u <username> /var/spool/cron/crontab/<username>')
	except:
		raise SystemExit	

else:
	print("Execution aborted as there was an error to query the api!")
