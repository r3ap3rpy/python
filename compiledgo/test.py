import ctypes

library = ctypes.cdll.LoadLibrary('./library.so')
hello_world = library.helloWorld
multiply = library.multiply


hello_world()
print(multiply(9,7))