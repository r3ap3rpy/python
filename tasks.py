from invoke import task, call

@task(name = "webopener")
def openwebpage(c, url = None):
    if url:
        c.run(f"start {url}")
    else:
        print("I need a url to run!")

@task
def firststep(c):
    print("Going to perform the first step!")

@task 
def thirdstep(c, name = "This is the default name!"):
    print("Going to perform the third step!")
    print(f"We go the argument name = {name}")

@task(pre = [firststep], post=[call(thirdstep, name = "This is chained!")])
def secondstep(c):
    print("This is the main happening!")

@task(name = "gitter")
def commitrepo(c, name = None, commit = "This is a change in the repository!"):
    if not name:
        print("You need a repository name to commit to!")
    else:
        c.run(r'cd c:\\Users\\r3ap3rpy\\Documents\\Youtube\\GitRepos\\{name} && git commit -a -m "{commit}"'.format(name = name, commit = commit))
        c.run(r'cd c:\\Users\\r3ap3rpy\\Documents\\Youtube\\GitRepos\\{name} && git push -u origin master'.format(name = name))
