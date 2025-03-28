import typer
import os
import importlib.util
import json

def validate(path: str):
    print(f"Validating module at: {path}")
    manifest_path = os.path.join(path, "manifest.json")
    if not os.path.exists(manifest_path):
        print("❌ Missing manifest.json")
        return

    try:
        with open(manifest_path) as f:
            manifest = json.load(f)
        if "name" not in manifest:
            print("❌ 'name' is missing in manifest.json")
            return
    except Exception as e:
        print(f"❌ Error reading manifest.json: {e}")
        return

    module_folder = os.path.join(path, manifest["name"])
    init_file = os.path.join(module_folder, "__init__.py")
    if not os.path.exists(init_file):
        print("❌ Missing __init__.py")
        return

    spec = importlib.util.spec_from_file_location("module", init_file)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"❌ Failed to load module: {e}")
        return

    if not hasattr(module, "register"):
        print("❌ Module is missing 'register(app)' function")
        return

    print("✅ Module looks good!")
