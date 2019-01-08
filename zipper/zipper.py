import zipfile
import sys

with zipfile.ZipFile(f"{sys.argv[1]}.zip","w") as myzip:
	for file in sys.argv[2:]:
		myzip.write(file)