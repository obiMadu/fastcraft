import typer
import time
from rich import print
from rich.progress import Progress, 
from InquirerPy import get_style
from pathlib import Path
import subprocess
from fastcraft.utils.generate_file_struct import generate_file_structure
from fastcraft.utils.choices import get_orm_choice
from fastcraft.utils.package_manager import initialize_packages
from typing_extensions import Annotated


create_dir = typer.Typer()



@create_dir.command()
def init(
    projectname: Annotated[str, typer.Argument(help="Start a new FastAPI Project")]
):
    """
    Start a new FastAPI project 
    """
    base_dir = Path.cwd() / projectname
    
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
    ):
     
        if step == "Creating project folder structure":
            generate_file_structure(projectname, orm_choice)
       
            
        if step == "Initiating Project and Installing dependencies with uv":
            initialize_packages(projectname, orm_choice)
         
            
    typer.echo(f"✅ FastAPI project '{projectname}' has been created at {base_dir}")
    print(f"🎉 Project '{projectname}' is ready!")
