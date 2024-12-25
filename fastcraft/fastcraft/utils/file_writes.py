from pathlib import Path


def write_schemas_file(projectname: str):
    base_dir = Path.cwd() / projectname
    schemas_file = base_dir / "app" / "schemas" / "schemas.py"
    schemas_file.parent.mkdir(parents=True, exist_ok=True)
    
    schemas_file.write_text(
        """from pydantic import BaseModel\n\n"""
        """class Item(BaseModel):\n"""
        """    name: str\n"""
        """    description: str = None\n""",
        encoding="utf-8"
    )
    
    return schemas_file

def write_main_file(projectname):
    base_dir = Path.cwd() / projectname
    main_file = base_dir / "app" / "main.py"
    main_file.parent.mkdir(parents=True, exist_ok=True)
    
    main_file.write_text(
        """from fastapi import FastAPI\n\n"""
        """app = FastAPI()\n\n"""
        """@app.get("/")\n"""
        """def read_root():\n"""
        """    return {"message": "Hello, FastForge!"}\n""",
        encoding="utf-8"
    )
    
    return main_file
