from collections import UserList

class MyList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"{prefix} {value} "

l = MyList((1,2,3,4,5,6,7,8,9,10))

print(l[0])
print(l[2])
print("".join(l))