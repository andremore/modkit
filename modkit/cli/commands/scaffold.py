import typer
import os

def scaffold(name: str, with_api: bool = False, with_model: bool = False):
    print(f"Scaffolding new module: {name}")
    os.makedirs(f"{name}/{name}", exist_ok=True)

    # __init__.py
    with open(f"{name}/{name}/__init__.py", "w") as f:
        f.write("def register(app):\n    return {}\n")

    # manifest.json
    with open(f"{name}/manifest.json", "w") as f:
        f.write('{"name": "' + name + '"}\n')

    if with_api:
        with open(f"{name}/{name}/api.py", "w") as f:
            f.write("from fastapi import APIRouter\n\nrouter = APIRouter()\n\n@router.get('/')\ndef read_root():\n    return {'message': 'Hello from " + name + "'}\n")

    if with_model:
        with open(f"{name}/{name}/models.py", "w") as f:
            f.write("from modkit import Base\nfrom sqlalchemy import Column, Integer, String\n\nclass Example(Base):\n    __tablename__ = 'example'\n    id = Column(Integer, primary_key=True)\n    name = Column(String)\n")

    print("✅ Module scaffolded.")
