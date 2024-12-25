from InquirerPy import inquirer

def get_orm_choice():
    """
    Prompt the user to select the database ORM to use.
    Returns:
        str: The selected ORM (e.g., 'sqlalchemy', 'sqlmodel').
    """
    try:
        return inquirer.select(
                message  = "Select the database ORM to use:",
                choices = [
                    {'name': "SQLAlchemy", "value": "sqlalchemy"},
                    {'name': "SQLModel", "value": "sqlmodel"},
                ],
                default ="sqlmodel",
                
            ).execute()
    except Exception as e:
        print(f"[red]❌ Error: {e}[/red]")
        raise typer.Exit(code=1)