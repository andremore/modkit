import typer
from modkit import modkit_config

def uninstall(name: str):
    if modkit_config.remove_module(name):
        print(f"🗑️  Uninstalled '{name}'")
    else:
        print(f"❌ Module '{name}' not found.")
