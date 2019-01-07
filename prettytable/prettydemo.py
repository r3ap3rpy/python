import prettytable
import sqlite3

Pretty = prettytable.PrettyTable()

x.add_column('HeroNames',['Drow Range','BeastMaster','Centaur','Daemon Witch'])
x.add_column('Health',[600,700,800,600])
x.add_column('Mana',[200,200,180,300])


x.add_row(['Barathrum',1000,200])

DB.connect('Heroes.db')
cur = DB.cursor()
cur.execut('SELECT * FROM Heroes')
print(prettytable.from_db_cursor(cur.execute('SELECT * FROM Heroes')))