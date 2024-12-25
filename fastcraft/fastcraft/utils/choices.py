

def get_orm_choice():
    orm_choice = inquirer.select(
            message  = "Select the database ORM to use:",
            choices = [
                {'name': "SQLAlchemy", "value": "sqlalchemy"},
                {'name': "SQLModel", "value": "sqlmodel"},
            ],
            default ="sqlmodel",
            
        ).execute()