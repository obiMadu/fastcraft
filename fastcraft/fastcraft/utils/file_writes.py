from pathlib import Path

base_dir = Path.cwd() / projectname

def schemas_file_path():
    schemas_file = base_dir / "app" / "schemas" / "schemas.py"
    schemas_file.write_text(
        """from pydantic import BaseModel\n\n"""
        """class Item(BaseModel):\n"""
        """    name: str\n"""
        """    description: str = None\n""",
        encoding="utf-8"
    )
    
    return schemas_file