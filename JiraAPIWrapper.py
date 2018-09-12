from jira import JIRA
import requests
 requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
 class JiraException(Exception):
	pass
 class Jira(object):
	__options = {
		'server':'<protocols>://<your.company.com>',
		'verify':False
	}
	__client = None
 	def __init__(self, **kwargs):
		if len(kwargs) != 2:
			raise JiraException('In order to use this class you need to specify a user and a password as keyword arguments!')
		else:
			if 'username' in kwargs.keys():
				self.__username = kwargs['username']
			else:
				raise JiraException('You need to specify a username as keyword argument!')
 			if 'password' in kwargs.keys():
				self.__password = kwargs['password']
			else:
				raise JiraException('You need to specify a password as keyword argument!')
			
			try:
				self.__client = JIRA(self.__options, basic_auth=(self.__username, self.__password))
			except:
				raise JiraException('Could not connect to the API, invalid username or password!') from None
 	def __str__(self):
		return 'Jira(username = {}, password = {}, endpoint = {}'.format(self.__username, self.__password, self.__options['server'])
	
	def __repr__(self):
		return 'Jira(username = {}, password = {}, endpoint = {}'.format(self.__username, self.__password, self.__options['server'])
	
	def __format__(self, r):
		return 'Jira(username = {}, password = {}, endpoint = {}'.format(self.__username, self.__password, self.__options['server'])
	
	def getProjects(self, raw = False):
		Projects = []
		for project in self.__client.projects():
			if raw:
				Projects.append(project)
			else:
				Projects.append({ 'Name':project.key, 'Description':project.name })
		return Projects
 	def getIssues(self, maxResults = 10, raw = False, **kwargs):
		Issues = []
		if len(kwargs) < 1:
			raise JiraException('You need to specify a search criteria!')
		else:
			searchstring = ' '.join([( _ + "=" + kwargs[_]) if _ != 'condition' else kwargs[_] for _ in kwargs])
			for item in self.__client.search_issues(searchstring, maxResults = maxResults):
				if raw:
					Issues.append(item)
				else:
					Issues.append({'Assignee':item.fields.assignee,'TimeSpent':item.fields.timespent,'CreateDate':item.fields.created,'DueDate':item.fields.duedate,'ResolutionDate':item.fields.resolutiondate,'Status':item.fields.status,'Peer Reviewer':item.fields.customfield_13307,'Reporter':item.fields.reporter,'Name':str(item), 'Summary':item.fields.summary, 'Description':item.fields.description})
		return Issues
 	def transition(self, issue, transition):
		pass
 	def new_issue(self, **kwargs):
		pass
 	def comment_issue(self, issue, comment)
if __name__ == '__main__':
	MyJira = Jira(username='MyUser', password='MyPassword')
	print(MyJira.getProjects())
	print(MyJira.getIssues(project='MyProject',condition='AND',status='Closed')) 