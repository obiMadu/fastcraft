from pathlib import Path
import os

def generate_file_structure(projectname: str, orm_choice: str):
    """
    Generate a basic folder structure for a FastAPI project, considering cross-platform compatibility.
    """
    base_dir = Path.cwd() / projectname

    # Define the folder structure
    folders = [
        "app",
        "app/routers",
        "app/models",
        "app/core",
        "app/utils",
        "tests"
    ]
    
    # If ORM choice given by the user is SQLAlchemy, include the shemas folder in the scaffold
    if orm_choice == 'SQLAlchemy':
       folder.append("app/shemas")
        
    # Create the directories
    for folder in folders:
        dir_path = base_dir / folder
        dir_path.mkdir(parents=True, exist_ok=True)

    # Create a basic main.py file
    
    if orm_choice == 'SQLAlchemy':
        schemas_file_path = base_dir / "app" / "schemas" / "schemas.py"
        schemas_file_path.write_text(
            """from pydantic import BaseModel\n\n"""
            """class Item(BaseModel):\n"""
            """    name: str\n"""
            """    description: str = None\n""",
            encoding="utf-8"
        )
    
    main_file_path = base_dir / "app" / "main.py"
    main_file_path.write_text(
        """from fastapi import FastAPI\n\n"""
        """app = FastAPI()\n\n"""
        """@app.get("/")\n"""
        """def read_root():\n"""
        """    return {"message": "Hello, FastForge!"}\n""",
        encoding="utf-8"
    )

    print(f"✅ Basic FastAPI project '{projectname}' has been created at {base_dir}")
