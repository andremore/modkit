import typer
from modkit import modkit_config

def disable(name: str):
    mod = modkit_config.get_module(name)
    if not mod:
        print(f"❌ Module '{name}' is not installed.")
        return
    mod["enabled"] = False
    modkit_config.update_module(name, mod)
    print(f"✅ Disabled '{name}'")
