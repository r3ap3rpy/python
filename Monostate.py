class MonoState(object):
	__internal_state = {'A':5,'B':6}

	def __init__(self):
		self.__dict__ = self.__internal_state


class MonoState_v2(object):
	_internal_state = {}
	def __new__(cls, *args, **kwargs):
		obj = super(MonoState_v2, cls).__new__(cls, *args, **kwargs)
		obj.__dict__ = cls._internal_state
		return obj

A = MonoState_v2()
B = MonoState_v2()

A.x = 10
B.x = 20

print(id(A.x))
print(id(B.x))

print('A object: {}'.format(A))
print('B object: {}'.format(B))

print('A object state: {}'.format(A.__dict__))
print('B object state: {}'.format(B.__dict__))