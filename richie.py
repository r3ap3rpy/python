from rich.console import Console

rc = Console()

rc.print(f"Welcome to my youtube channel!", style = "underline green")
rc.print({'a':1,'b':2,'c':3})
rc.print([1,2,3,4,5])
rc.print(f"[underline green]Welcome[/underline green] to my [bold red]youtube channel![/bold red]")

rc.print(f":thumbs_up: You are learning richie!")
rc.print(f":vampire:'s dont like garlic!")
