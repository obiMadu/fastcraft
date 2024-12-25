import typer
import time
from rich import print
from rich.progress import track
from InquirerPy import get_style
from pathlib import Path
import subprocess
from fastcraft.utils.generate_file_struct import generate_file_structure
from fastcraft.utils.choices import get_orm_choice
from fastcraft.utils.package_manager


create_dir = typer.Typer()



@create_dir.command()
def init(projectname: str):
    base_dir = Path.cwd() / projectname
    """
    Start a new FastAPI project 
    User can choose between SQLAlchemy or SQLModel for database setup.
    """
    if base_dir.exists():
        print(f"[red]❌ Error: A project named '{projectname}' already exists in the current directory.[/red]")
        raise typer.Exit(code=1)
    
    orm_choice = get_orm_choice()
    steps = [
        "Creating project folder structure",
        "Initiating Project and Installing dependencies with uv"
        
    ]
    for step in track(
        steps, 
        description=f"[cyan]Setting up '{projectname}'...",
        
    ):
     
        if step == "Creating project folder structure":
            generate_file_structure(projectname, orm_choice)
            time.sleep(1)
            
        if step == "Initiating Project and Installing dependencies with uv":
            
    typer.echo(f"✅ FastAPI project '{projectname}' has been created at {base_dir}")
    print(f"🎉 Project '{projectname}' is ready!")
