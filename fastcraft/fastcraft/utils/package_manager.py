import subprocess
from rich import print
from pathlib import Path
import typer

def initialize_packages(projectname: str):
    try:
        subprocess.run(
            [
                "uv",
                "init",
            ],
            check=True,
            cwd=projectname
            
        )
        subprocess.run(
            [
                "uv",
                "add",
                "fastapi"
            ],
            check=True,
       
            
            
        )
        print(f"[green]✅ Dependencies installed successfully![/green]")
    except subprocess.CalledProcessError as e:      
        print(f"[red]❌ Error during dependency installation: {e}[/red]")
        raise typer.Exit(code=1)
        