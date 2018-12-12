import argparse
import os
import ast
from github import Github

parser = argparse.ArgumentParser(description = "This is a gister demo for youtube!")
parser.add_argument('--gistid',metavar = "GISTID", type = str, help = "This is the ID of the gist!")
arguments = parser.parse_args()

if arguments.gistid:
	GTHB = Github(os.getenv('GUSER'),os.getenv('GPASS'))
	gister = GTHB.get_gist(arguments.gistid)
	for key in gister.files.keys():
		print(f'Executing the file: {key} from gists of github!')
		exec(compile(ast.parse(gister.files[key].content), filename = key, mode = 'exec'))

else:
	parser.print_help()