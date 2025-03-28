import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "modkit_config.json")

def _load_config():
    if not os.path.exists(CONFIG_PATH):
        return {"installed_modules": {}}
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def _save_config(data):
    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f, indent=2)

def get_module(name: str):
    data = _load_config()
    return data["installed_modules"].get(name)

def update_module(name: str, module_info: dict):
    data = _load_config()
    data["installed_modules"][name] = module_info
    _save_config(data)

def remove_module(name: str):
    data = _load_config()
    if name in data["installed_modules"]:
        del data["installed_modules"][name]
        _save_config(data)
        return True
    return False

def get_all_modules():
    data = _load_config()
    return data["installed_modules"]
