import typer
from modkit import modkit_config

def enable(name: str):
    mod = modkit_config.get_module(name)
    if not mod:
        print(f"❌ Module '{name}' is not installed.")
        return
    mod["enabled"] = True
    modkit_config.update_module(name, mod)
    print(f"✅ Enabled '{name}'")
