from fabric import task

@task
def Hello(c):
    print("Hello World")

@task
def massCopy(c,files):
    toBeCopied = []
    if ',' in files:
        toBeCopied = files.split(',')
    else:
        toBeCopied.append(files)
    
    for file in toBeCopied:
        print(f"The file: {file} will be copied to: {c.host}")
        c.put(file, remote = f"/tmp/{file}")