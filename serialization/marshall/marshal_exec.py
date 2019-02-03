import marshal

script = """
for i in range(10):
	print(i)
"""

code = compile(script,'<script>','exec')

with open('exec.marshal','wb') as exec_file:
	marshal.dump(code,exec_file)


#with open('exec.marshal', 'rb') as marsh_file:
#	code = marshal.load(marsh_file)
#exec(code)