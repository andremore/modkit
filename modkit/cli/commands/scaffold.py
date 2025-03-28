import typer
import os

def scaffold(name: str):
    print(f"Scaffolding new module: {name}")
    os.makedirs(f"{name}/{name}", exist_ok=True)
    with open(f"{name}/{name}/__init__.py", "w") as f:
        f.write("def register(app):\n    return {}\n")
    with open(f"{name}/manifest.json", "w") as f:
        f.write('{"name": "' + name + '"}\n')
    print("Module scaffolded.")
