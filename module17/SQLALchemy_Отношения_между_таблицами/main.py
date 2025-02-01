from sqlalchemy.schema import CreateTable
from app.database import engine
from app import User, Task

print("SQL для User:")
print(CreateTable(User.__table__).compile(engine))

print("\nSQL для Task:")
print(CreateTable(Task.__table__).compile(engine))