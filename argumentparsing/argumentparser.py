import argparse

parser = argparse.ArgumentParser(description = "This a demo for the argparse module!")
parser.add_argument('--tobesummed',metavar = "INTLIST", type = int, nargs = "+", help = "The list of integers")
arguments = parser.parse_args()


if arguments.tobesummed:
	print("The sum of the list is: {}".format(sum(arguments.tobesummed)))
else:
	parser.print_help()