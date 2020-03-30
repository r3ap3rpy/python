import configparser
from pprint import pprint
parser = configparser.RawConfigParser()
parser.read(r"D:\GitRepos\python\test.con")

expected =  ["user","pass"]

for i in parser.keys():
    print(i)

for i in parser.keys():
    print(parser[i])

data = {}
for i in parser.keys():
    if i == 'DEFAULT':
        continue
    data[i] = {}
    print(f"The section is: {i}")
    for expect in expected:
        print(f"{expect} = {parser[i][expect]}")
        data[i][expect] = parser[i][expect]


pprint(data)
