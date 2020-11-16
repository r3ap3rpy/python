import os
import signal
import time

CWD = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])
PID = os.path.sep.join([CWD,'PID'])
PIDFILE = os.path.sep.join([PID,'pidfile'])
MYPID = os.getpid()
print(MYPID)
if os.path.isfile(PIDFILE):
        print("We have something to kill")
        try:
                with open(PIDFILE,'r') as pidfile:
                        OLDPID = int(pidfile.read())
        except Exception as e:
                OLDPID = None
                print(f"Could not convert the pid: {e}")
        if OLDPID:
                try:
                        os.kill(OLDPID,signal.SIGKILL)
                        print("Successfully killed the old process!")
                except ProcessLookupError as e:
                        print("No such process!")
                except Exception as e:
                        print(f"Failed to kill the old process because: {e}")
                        raise SystemExit
        else:
                print("The older process cannot be found!")

else:
        print("There is no previous instance running at the moment!")

with open(PIDFILE,'w') as pidfile:
        pidfile.write(str(MYPID))

time.sleep(30)


if os.path.isfile(PIDFILE):
        try:
                os.remove(PIDFILE)
                print("The lock has been removed!")
        except:
                print("The remove has failed!")

else:
        print("No pid to remove!")