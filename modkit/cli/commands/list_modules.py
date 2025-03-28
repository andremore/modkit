import typer
from modkit import modkit_config

def list_modules():
    modules = modkit_config.get_all_modules()
    if not modules:
        print("No modules installed.")
        return
    for name, data in modules.items():
        status = "✅ enabled" if data.get("enabled") else "⛔ disabled"
        print(f"{name:20} {status}")
