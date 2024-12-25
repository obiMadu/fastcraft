import typer
from rich import print
from InquirerPy import inquirer
from fastcraft.utils.generate_file_struct import generate_file_structure


create_dir = typer.Typer()


@create_dir.command()
def init(projectname: str):
    """
    Start a new FastAPI project 
    User can choose between SQLAlchemy or SQLModel for database setup.
    """
    print(f"🚀 Starting new project: {projectname}")
    
    orm_choice = inquirer.select(
        message  = "Select the database ORM to use:",
        choices = [
            {'name': "SQLAlchemy", "value": "sqlalchemy"},
            {'name': "SQLModel", "value": "sqlmodel"},
        ],
        default ="sqlmodel"
        
    ).execute()
        
    generate_file_structure(projectname, orm_choice)
    print(f"🎉 Project '{projectname}' is ready!")
