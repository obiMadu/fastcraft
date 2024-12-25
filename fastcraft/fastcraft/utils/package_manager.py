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
                projectname
            ],
            check=True,
            cwd = Path.cwd()
        )
        subprocess.run(
            [
                "uv",
                "add",
                "fastapi"
            ],
            check=True,
            cwd = Path.cwd()
        )
    except subprocess.CalledProcessError as e:      
        print(f"[red]❌ Error during dependency installation: {e}[/red]")
        raise typer.Exit(code=1)
        