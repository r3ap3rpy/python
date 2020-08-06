from time import sleep
from rich.progress import Progress

p = Progress()

for i in p.track(range(1,31)):
    p.log(f":thumbs_up: we are making progress : {i}")
    sleep(0.5)
