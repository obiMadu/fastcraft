import typer
import time
from rich import print
from rich.progress import track
from InquirerPy import get_style
from pathlib import Path
from fastcraft.utils.generate_file_struct import generate_file_structure
from fastcraft.utils.choices import get_orm_choice


create_dir = typer.Typer()


@create_dir.command()
def init(projectname: str):
    base_dir = Path.cwd() / projectname
    """
    Start a new FastAPI project 
    User can choose between SQLAlchemy or SQLModel for database setup.
    """
    
    

    orm_choice = get_orm_choice()
    steps = [
        "Creating project folder structure","Generating main.py file",
        "Generating schemas.py (if applicable)",
        "Finalizing project setup",
    ]
    for step in track(steps, description=f"[green]Setting up '{projectname}'..."):
     
        if step == "Creating project folder structure":
            generate_file_structure(projectname, orm_choice)
            time.sleep(2)
    typer.echo(f"✅ Basic FastAPI project '{projectname}' has been created at {base_dir}")
    print(f"🎉 Project '{projectname}' is ready!")
