from rich.console import Console
from rich.theme import Theme
from time import sleep
ct = Theme({
    'good' : "bold green",
    'bad' : "red underline"
})

rc = Console(theme = ct)
rc.print("[bad]Welcome[/bad] to the second [good]video![/good]")

for i in range(10):
    vampire = {"vitality":i*10,'hunger':(100 - i* 10)}
    rc.log(f":vampire: is at feeding : {i}")
    sleep(1)
    rc.log(f":vampire: is satisfied :thumbs_up:", log_locals = True)
