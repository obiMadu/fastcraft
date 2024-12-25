import subprocess
from rich import print
from pathlib import Path
import typer

def initialize_packages(projectname: str, orm_choice: str):
    try:
        subprocess.run(
            [
                "uv",
                "init",
            ],
            check=True,
            cwd=projectname
            
        )
        if orm_choice == 'sqlalchemy':
        subprocess.run(
            [
                "uv",
                "add",
                "fastapi"
            ],
            check=True,
            cwd=projectname
            
            
        )
        print(f"[green]✅ Dependencies installed successfully![/green]")
    except subprocess.CalledProcessError as e:      
        print(f"[red]❌ Error during dependency installation: {e}[/red]")
        raise typer.Exit(code=1)
        