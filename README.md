# Modkit

`modkit` is a lightweight developer toolkit for building external FastAPI modules that can be dynamically registered into a modular system.

## Features

- Shared `Base`, `engine`, `get_db` utilities
- Typed `ModuleContract` for clean DX
- Optional `runtime_context` for shared communication

## Installation

### From GitHub

```bash
pip install git+https://github.com/your-org/modkit.git@main
```

### Usage in External Modules

```python
from modkit import Base, get_db
from modkit.types import AppType, ModuleContract

def register(app: AppType) -> ModuleContract:
    from .models import Invoice
    from .api import router

    app.include_router(router, prefix="/invoices")

    return {
        "models": [Invoice],
    }
```
