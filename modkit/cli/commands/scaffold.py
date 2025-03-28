import typer
import os

def scaffold(name: str, interactive: bool = True, with_api: bool = False, with_model: bool = False):
    if interactive:
        with_api = typer.confirm("Do you want to generate an API file?", default=True)
        with_model = typer.confirm("Do you want to generate a model file?", default=True)

    print(f"📦 Scaffolding new module: {name}")
    os.makedirs(f"{name}/{name}", exist_ok=True)

    # __init__.py
    with open(f"{name}/{name}/__init__.py", "w") as f:
        f.write("def register(app):\n    return {}\n")

    # manifest.json
    with open(f"{name}/manifest.json", "w") as f:
        f.write(f'{{"name": "{name}"}}\n')

    if with_api:
        with open(f"{name}/{name}/api.py", "w") as f:
            f.write(
                "from fastapi import APIRouter\n\n"
                "router = APIRouter()\n\n"
                "@router.get('/')\n"
                "def read_root():\n"
                f"    return {{'message': 'Hello from {name}'}}\n"
            )

    if with_model:
        with open(f"{name}/{name}/models.py", "w") as f:
            f.write(
                "from modkit import Base\n"
                "from sqlalchemy import Column, Integer, String\n\n"
                "class Example(Base):\n"
                "    __tablename__ = 'example'\n"
                "    id = Column(Integer, primary_key=True)\n"
                "    name = Column(String)\n"
            )

    print("✅ Done!")
