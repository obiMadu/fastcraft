import typer
from rich import print
from rich.progress import track
from InquirerPy import get_style
from fastcraft.utils.generate_file_struct import generate_file_structure
from fastcraft.utils.choices import get_orm_choice


create_dir = typer.Typer()


@create_dir.command()
def init(projectname: str):
    """
    Start a new FastAPI project 
    User can choose between SQLAlchemy or SQLModel for database setup.
    """
    print(f"🚀 Starting new project: {projectname}") 
    orm_choice = get_orm_choice()
    steps = [
        "Creating project folder structure with information specified",
    ]
    for step in track(steps, description=f"[cyan]Setting up '{projectname}'..."):
        if step == "Creating project folder structure":
            generate_file_structure(projectname, orm_choice)

    print(f"🎉 Project '{projectname}' is ready!")
