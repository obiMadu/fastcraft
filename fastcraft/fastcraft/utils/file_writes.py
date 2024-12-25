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