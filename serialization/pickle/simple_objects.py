import pickle

a = 10

my_list = [1,2,3,b"pickle is cool", "Python is coller"]

my_dict = {
	"Name" : "Daniel",
	"Age" : 28,
	"Gender" : "Pythonista"
}

with open('my_dict.pickle', "wb") as a_file:
	pickle.dump(my_dict, a_file, pickle.HIGHEST_PROTOCOL)