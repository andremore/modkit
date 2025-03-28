import typer
import os

from modkit.templates import models_template, api_template, init_template, manifest_template


def scaffold(name: str, interactive: bool = True, with_api: bool = False, with_model: bool = False):
    class_name = "".join(word.capitalize() for word in name.replace("-", "_").split("_"))
    table_name = name.replace("-", "_").lower()

    if interactive:
        with_api = typer.confirm("Do you want to generate an API file?", default=True)
        # model is implied if API is generated

    print(f"📦 Scaffolding new module: {name}")
    os.makedirs(f"{name}/{name}", exist_ok=True)

    # __init__.py
    with open(f"{name}/{name}/__init__.py", "w") as f:
        f.write(init_template.render())

    # manifest.json
    with open(f"{name}/manifest.json", "w") as f:
        f.write(manifest_template.render(table_name))

    # models.py (always created if API is selected)
    if with_api or with_model:
        with open(f"{name}/{name}/models.py", "w") as f:
            f.write(models_template.render(class_name, table_name))

    # api.py
    if with_api:
        with open(f"{name}/{name}/api.py", "w") as f:
            f.write(api_template.render(class_name, table_name))

    print("✅ Done!")
