import subprocess
from rich import print

def initialize_packages(projectname: str):
    try:
        subprocess.run
    except subprocess.CalledProcessError as e:      
        print(f"[red]❌ Error during depen: {e}[/red]")
        