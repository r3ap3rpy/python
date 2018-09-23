class A(object):
	def method(self):
		print('I am from class A')

class B(A):
	def method(self):
		print('I am from class B')

class C(A):
	def method(self):
		print('I am from class C')

class D(C,B):
	pass

d = D()
d.method()
print(D.mro())