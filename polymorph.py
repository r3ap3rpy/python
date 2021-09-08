from functools import singledispatch

@singledispatch
def helloWorld(arg):
    print(arg)

@helloWorld.register
def _(arg: int):
    print("We are executing with <int> arguments!")
    print(arg)

@helloWorld.register
def _(arg: str):
    print("We are executing with <str> arguments!")
    print(arg)

@helloWorld.register
def _(arg: list):
    print("We are executing with <list> arguments!")
    print(arg)

helloWorld(1)
helloWorld("mystring")
helloWorld(list((1,2,3,4,5)))