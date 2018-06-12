from jira import JIRA
import requests
import os
import argparse


requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

__options = {
	'server':'https://nijira.natinst.com',
	'verify':False
}

__Components = {
'17436':'AEM',
'15235':'Akamai',
'23607':'Ansible',
'15236':'Apache',
'15237':'APEX',
'15501':'Attivio',
'23606':'AWS',
'15238':'Backups',
'15239':'Citrix / XenApp',
'15240':'Core Network',
'15502':'Cron',
'19685':'dap',
'15241':'Data Center',
'15242':'Data Warehouse',
'15243':'Database',
'15244':'DataSource',
'15900':'Deploy Request',
'15245':'DNS Server',
'15246':'DNS-External',
'15247':'DNS-Internal',
'15248':'Domain Controller',
'15249':'Domino Application',
'16212':'FAST',
'15250':'Folder Share',
'15251':'FTP',
'15252':'Gomez',
'23636':'Grafana',
'15253':'HP Project and Portfolio Management (PPM)',
'15254':'HP Service Manager',
'17500':'IDM',
'15255':'Internet Network',
'15256':'IP',
'15257':'JIRA IT',
'15258':'JIRA TMD',
'15259':'Jive SBS',
'15260':'LDAP (Active Directory)',
'15261':'Licensing',
'17125':'LoadRunner',
'15262':'Lotus Notes',
'15263':'Men&Mice',
'15264':'Microsoft Internet Information Server (IIS)',
'15265':'Nagios',
'15266':'NetScaler',
'15267':'Network Management/Monitoring',
'15268':'NI Talk',
'23634':'OpenTSDB',
'15269':'Oracle',
'17124':'OSB',
'15270':'Panorama',
'15271':'Perforce',
'15272':'PKI / Certificate',
'15816':'Project',
'15273':'Reports',
'15274':'Samba',
'15275':'Sametime',
'15276':'SAN',
'15277':'Security',
'15278':'Server',
'15279':'Server Network',
'15280':'Service Desk',
'15281':'SiteScope',
'19402':'soa',
'15282':'Splunk',
'18027':'Splunk, Aem',
'23603':'SSL Certificate',
'23604':'Sterling',
'15283':'Storage NetApp',
'23635':'tcollector',
'23605':'Trash',
'15284':'TrueSight',
'15285':'Unix',
'15286':'User Administration',
'15287':'VCM',
'15288':'Virus/Malware',
'15289':'VPN',
'15290':'VPN Network',
'15291':'WAN Network',
'15292':'Web Based Training',
'15293':'Web Systems',
'15294':'WebAdminApp',
'15295':'Webdisk',
'15296':'WebEx',
'15297':'WebLogic',
'17501':'Websphere eCommerce',
'15298':'Windows Active directory',
'15299':'Windows Server OS',
'19691':'wrapper',
'15300':'YourKit'
}

JIRAUSER = None
JIRAPASS = None
JIRASESS = None
COMPID = '15293'
issueToComment = None
issueToClose = None

parser = argparse.ArgumentParser('Tool to document your actions via Jira Tickets!')
parser.add_argument("-u","--user",type=str,help="Specifies the user to use!")
parser.add_argument("-p","--password",type=str,help="Specifies the password to use!")
parser.add_argument("-s","--summary",type=str,help="Specifies the summary to use!")
parser.add_argument("-d","--description",type=str,help="Specifies the description to use!")
parser.add_argument("-comp","--component",type=str,help="Specifies the component to use!")
parser.add_argument("-c","--closure",type=str,help="Specifies the closure comments to use!")

parser.add_argument("-close","--close",type=str,help="Specifies the close action item to use!")
parser.add_argument("-comment","--comment",type=str,help="Specifies the comment action item to use!")
args= parser.parse_args()

print('[+][-][-][-][-][-][-][-][-]')
if args.user is None:
	print('[+] Using JIRAUSER from ENV!')
	JIRAUSER = os.getenv('JIRAUSER')
	if JIRAUSER is None:
		print('[-] Failed to load JIRAUSER from ENV, aborting!')
		raise SystemExit
	else:
		print('[+] Loaded username: {}'.format(JIRAUSER))
else:
	print('[+] Using specified JIRAUSER: {}'.format(args.user))
	JIRAUSER = args.user

if args.password is None:
	print('[+] Using JIRAPASS from ENV!')
	JIRAPASS = os.getenv('JIRAPASS')
	if JIRAPASS is None:
		print('[-] Failed to load JIRAPASS from ENV, aborting!')
		raise SystemExit
	else:
		print('[+] Loaded password: ******')
else:
	print('[+] Using specified JIRAPASS: ******')
	JIRAPASS = args.password


if args.close is not None:
	print('[+] Ticket with this ID: {} will be closed if found!'.format(args.close))
	if args.closure is None:
		print('[-] Error, closure comments not specified!')
		print('[+][-][-][-][-][-][-][-][-]')
		raise SystemExit

elif args.comment is not None:
	print('[+] New comment to this ticket: {} will be added if found!'.format(args.comment))
	if args.closure is None:
		print('[-] Error, comments not specified!')
		print('[+][-][-][-][-][-][-][-][-]')
		raise SystemExit
else:
	if args.summary is None:
		print('[-] Error, a summary must be specified!!')
		print('[+][-][-][-][-][-][-][-][-]')
		raise SystemExit
	if args.description is None:
		print('[-] Error, a description must be specified!!')
		print('[+][-][-][-][-][-][-][-][-]')
		raise SystemExit
	if args.closure is None:
		print('[*] Closure comments not specified!')
		print('[*] Ticket will be opened only!')
	if args.component is None:
		print('[*] Component was not specified!')
		print('[*] Defaulting to <Web Systems> component!')
	else:
		for com in __Components:
			if __Components[com] == args.component:
				COMPID = com
				break
		else:
			print('[-] Could not find the specified component!')
			print('[-] Valid components are: {}'.format(','.join([__Components[_] for _ in __Components])))
			print('[+][-][-][-][-][-][-][-][-]')
			raise SystemExit

try:
	JIRASESS = JIRA(__options, basic_auth=(JIRAUSER,JIRAPASS))
except:
	print('[-] Could not login!')

if JIRASESS is None:
	print('[+][-][-][-][-][-][-][-][-]')
	raise SystemExit

if args.comment is not None:
	try:
		issueToComment = JIRASESS.search_issues('id={}'.format(args.comment))
		print('[+] Issue was found!')
	except:
		print('[-] Could not find issue with specified name: {}'.format(args.comment))

	if issueToComment is None:
		print('[+][-][-][-][-][-][-][-][-]')
		raise SystemExit

	print('[+] Adding comment to issue!')

	try:
		JIRASESS.add_comment(issueToComment[0],args.closure)
		print('[+] Successfully commented on the issue!')
	except:
		print('[-] Could not add comment to the issue!')

elif args.close is not None:
	try:
		issueToClose = JIRASESS.search_issues('id={}'.format(args.close))
		print('[+] Issue as found!')
	except:
		print('[-] Could not find issue with specified name: {}'.format(args.close))

	print('[+] Current status of the issue: {}'.format(issueToClose[0].fields.status))
	if not str(issueToClose[0].fields.status) in ['In Progress','Open']:
		print('[-] The issue is not in proper state, cannot transition!')
		print('[+][-][-][-][-][-][-][-][-]')
		raise SystemExit

	if len(issueToClose[0].fields.components) == 0:
		print('[*] Component is not set, applying the default component!')
		try:
			issueToClose[0].update(fields={'components': [{'id': COMPID}]})
			print('[+] Deafult component: {} was successfully applied!'.format(__Components[COMPID]))
		except:
			print('[-] Default component could not be applied, aborting!')
			print('[+][-][-][-][-][-][-][-][-]')
			raise SystemExit

	TransitionQueue = []
	if str(issueToClose[0].fields.status) == 'Open':
		TransitionQueue.append('Start Work')
		TransitionQueue.append('Close')
	else:
		TransitionQueue.append('Close')
	
	for item in TransitionQueue:
		print('[+] Transitioning issue to <{}>'.format(item))
		try:
			JIRASESS.transition_issue(issueToClose[0], transition=item)
			print('[+] Successfully transitioned the issue!')
		except:
			print('[-] Failed to transition the issue to <{}>'.format(item))
	print('[+][-][-][-][-][-][-][-][-]')
else:
	print('[+] Opening new issue!')
	try:
		new_issue = JIRASESS.create_issue(project='WSSUPPORT', summary=args.summary,description=args.description,components=[{'id':COMPID}],assignee={'name':JIRAUSER}, issuetype={'name':'Task'})
	except:
		print('[-] Error opening the new issue!')
	print('[+] New issue opened successfully: {}'.format(new_issue))

	print('[+] Transitioning issue to <Start Work>')
	try:
		JIRASESS.transition_issue(new_issue, transition='Start Work')
		print('[+] Successfully transitioned the issue!')
	except:
		print('[-] Failed to transition the issue to <Start Work>')

	if args.closure is None:
		print('[+][-][-][-][-][-][-][-][-]')
		pass
	else:
		print('[+] Adding closure comments!')
		try:
			JIRASESS.add_comment(new_issue,args.closure)
			print('[+] Successfully commented on the issue!')
		except:
			print('[-] Could not add comment to the issue!')

		print('[+] Transitioning the issue to <Closed>')
		try:
			JIRASESS.transition_issue(new_issue, transition='Close')
			print('[+] Successfully closed the issue!')
		except:
			print('[-] Failed to close the issue!')

		print('[+][-][-][-][-][-][-][-][-]')
