from rich.console import Console
from time import sleep

rc = Console(record = True)

rc.log("[blue]Welcome[/blue] to [green]rich![/green]")

for i in range(1,10):
    rc.log(":apple:"*i)
    try:
        if i > 8:
            raise ValueError("Too much!")
    except Exception as e:
        rc.log("Can't eat that much!")

rc.save_html('richie.html')

