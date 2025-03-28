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
Awesome! Here's a clean and simple `README.md` for your `modkit` repo — focused purely on relevant commands and what they're for:

---

```md
# Modkit CLI

Modkit is a CLI tool for managing and scaffolding modular FastAPI extensions. It helps developers scaffold, validate, run, and manage modules in a consistent, developer-friendly way.

## 🔧 Commands

### `modkit scaffold <name> [--with-api] [--with-model]`
Scaffold a new module with the given name. Optionally generate boilerplate API and/or model files.

> Example:
```bash
modkit scaffold blog --with-api
```

---

### `modkit validate <path>`
Validate that a module has a correct structure and a working `register()` function.

> Example:
```bash
modkit validate blog
```

---

### `modkit dev <path> [--port 8001]`
Run a module in an isolated FastAPI dev server. Great for testing routes locally.

> Example:
```bash
modkit dev blog
```

---

### `modkit install <name> <path>`
Install a local module and track it in the modkit config.

> Example:
```bash
modkit install blog ./blog
```

---

### `modkit enable <name>`
Enable a module (mark it as active in config).

> Example:
```bash
modkit enable blog
```

---

### `modkit disable <name>`
Disable a module (mark it as inactive in config).

> Example:
```bash
modkit disable blog
```

---

### `modkit uninstall <name>`
Remove a module from the modkit config.

> Example:
```bash
modkit uninstall blog
```

---

### `modkit list`
List all installed modules and show whether they're enabled or disabled.

> Example:
```bash
modkit list
```

---

## 📁 Output Structure

A scaffolded module will look like this:

```
blog/
├── manifest.json
└── blog/
    ├── __init__.py
    ├── api.py
    └── models.py
```

---

Let me know if you want a usage diagram or GIF in the future!

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
