from time import sleep

def loong():
    print("This will take some time!")
    sleep(3)
    a = []
    for i in range(10000000):
        a.append(i*i)
