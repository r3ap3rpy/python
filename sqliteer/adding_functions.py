import sqlite3

def tentimes(value):
	return value * 10

DB = sqlite3.connect('Add_Functions.db')
DB.create_function('tentimes', 1, tentimes)
cur = DB.cursor()

for row in cur.execute('SELECT item, net, tentimes(net) from Calculate'):
	print(row)