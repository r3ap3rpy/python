import os
import dis
import ast

os.system('cls')

while True:
	listoffiles = os.listdir('plugins')
	listoffiles.append('quit')
	listofcommands = [ _.split('.')[0] for _ in listoffiles]
	print('Welcome the the pluggable shell!')
	print('List of commands: ')
	for command in listofcommands:
		print('\t - {}'.format(command))

	answer = input('Tell me the command to run: ')

	if not answer:
		print('You did not specfiy a command!')
		os.system('cls')
		continue

	if answer not in listofcommands:
		print('The answer is incorrect: {}, see list of commands!'.format(answer))



	if answer == 'quit':
		raise SystemExit
	
	with open(os.path.sep.join(['plugins',(answer + '.py')]),'rb') as command_file:
		ast_of_command_file = ast.parse(command_file.read())

	code_of_command_file = compile(ast_of_command_file, filename = os.path.sep.join(['plugins',(answer + '.py')]), mode = 'exec')
	exec(code_of_command_file)
	input('Press enter to continue!')
	os.system('cls')
	

	