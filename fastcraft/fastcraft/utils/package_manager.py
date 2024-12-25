import subprocess
from rich import print
import typer

def initialize_packages(projectname: str):
    try:
        subprocess.run(
            [
                
            ]
        )
    except subprocess.CalledProcessError as e:      
        print(f"[red]❌ Error during dependency installation: {e}[/red]")
        raise typer.Exit(code=1)
        