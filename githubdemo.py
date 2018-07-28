from github import Github
from pprint import pprint
import os

guser = os.getenv('GUSER')
gpass = os.getenv('GPASS')

gpat = os.getenv('PAT')


GTHUB = Github(guser,gpass)

GTHUBKEY = Github(gpat)

REPOS = [ _ for _ in GTHUB.get_user().get_repos()]

print(REPOS)

print('API status: {}'.format(GTHUB.get_last_api_status_message().body))

print('Total public repos: {}'.format(GTHUB.get_user().public_repos))
print('Total private repos: {}'.format(GTHUB.get_user().total_private_repos))