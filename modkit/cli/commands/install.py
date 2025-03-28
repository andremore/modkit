import typer
import os
import json
from modkit import modkit_config

def install(name: str, path: str):
    if not os.path.exists(path):
        print(f"❌ Path '{path}' does not exist.")
        raise typer.Exit(1)

    manifest_path = os.path.join(path, "manifest.json")
    if not os.path.exists(manifest_path):
        print("❌ Missing manifest.json in the given path.")
        raise typer.Exit(1)

    with open(manifest_path) as f:
        try:
            manifest = json.load(f)
        except json.JSONDecodeError:
            print("❌ manifest.json is not valid JSON.")
            raise typer.Exit(1)

    mod_folder = os.path.join(path, name)
    if not os.path.exists(mod_folder):
        print(f"❌ Expected module folder '{mod_folder}' does not exist.")
        raise typer.Exit(1)

    modkit_config.update_module(name, {
        "enabled": False,
        "path": path,
        "source": "local"
    })

    print(f"✅ Installed local module '{name}' from {path}")
