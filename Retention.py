import pathlib
import os
import argparse

from datetime import datetime, timedelta

CWD = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])
OUTPUT = os.path.sep.join([CWD,'Output'])
FILETIMESTAMP = F"_{datetime.now().year}-{datetime.now().month}-{datetime.now().day}-{datetime.now().hour}-{datetime.now().minute}_"

parser = argparse.ArgumentParser(description='This script can be used to delete files from a specific folder after a gived retention time!')
parser.add_argument('-retentiontime','--retentiontime', type = int, default=7, help="The number of day(s) up to which the output should be kept, after that those are removed!", required=False)
args = parser.parse_args()

OldestPossibleDate = datetime.now() - timedelta(minutes=(args.retentiontime*1440))

print(f"##########################################")
print(f"The specified retention time is: {args.retentiontime}")
print(f"Checking if output folder exists!")
if not os.path.isdir(OUTPUT):
    print(f"There is no output folder!")
    print(f"##########################################")
    raise SystemExit
    
print(f"Looking for files in : {OUTPUT}")
OldFiles = os.listdir(OUTPUT)
if OldFiles:
    print(f"A total of {len(OldFiles)} file(s) were found, removing them if they are more that {args.retentiontime} day(s) old!.")
    print(f"Files created before: {str(OldestPossibleDate)} will be deleted!")
    for file in OldFiles:
        filename = os.path.sep.join([OUTPUT,file])
        fname = pathlib.Path(filename)
        mtime = datetime.fromtimestamp(fname.stat().st_mtime)
        print(f"The file: {filename.split('/')[-1]} was created on: {str(mtime)}")
        if OldestPossibleDate > mtime:
            print(f"Removing old file: {file}")
            os.remove(filename)
        else:
            print(f"Keeping file: {file} as the retention time is yet to be passed!")  
else:
    print("Output folder is empty...")

print(f"##########################################")