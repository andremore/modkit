import typer
import importlib.util
import os
import json
from fastapi import FastAPI
import uvicorn

def dev(path: str, port: int = 8001):
    print(f"Running dev server for module at: {path}")

    manifest_path = os.path.join(path, "manifest.json")
    with open(manifest_path) as f:
        manifest = json.load(f)
    name = manifest["name"]
    module_path = os.path.join(path, name, "__init__.py")

    spec = importlib.util.spec_from_file_location(name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    app = FastAPI()

    if hasattr(module, "register"):
        module.register(app)

    print(f"🚀 Starting dev server at http://localhost:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
