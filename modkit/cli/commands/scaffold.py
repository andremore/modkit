import typer
import os

def scaffold(name: str, interactive: bool = True, with_api: bool = False, with_model: bool = False):
    class_name = "".join(word.capitalize() for word in name.replace("-", "_").split("_"))
    table_name = name.replace("-", "_").lower()

    if interactive:
        with_api = typer.confirm("Do you want to generate an API file?", default=True)
        # model is implied if API is generated

    print(f"📦 Scaffolding new module: {name}")
    os.makedirs(f"{name}/{name}", exist_ok=True)

    # __init__.py
    with open(f"{name}/{name}/__init__.py", "w") as f:
        f.write("def register(app):\n    return {}\n")

    # manifest.json
    with open(f"{name}/manifest.json", "w") as f:
        f.write(f'{{"name": "{name}"}}\n')

    # models.py (always created if API is selected)
    if with_api or with_model:
        with open(f"{name}/{name}/models.py", "w") as f:
            f.write(
                "from modkit import Base\n"
                "from sqlalchemy import Column, Integer, String\n\n"
                f"class {class_name}(Base):\n"
                f"    __tablename__ = '{table_name}'\n"
                "    id = Column(Integer, primary_key=True)\n"
                "    name = Column(String)\n"
                "    description = Column(String)\n"
            )

    # api.py
    if with_api:
        with open(f"{name}/{name}/api.py", "w") as f:
            f.write(
                "from fastapi import APIRouter, HTTPException, Depends\n"
                "from sqlalchemy.orm import Session\n"
                f"from .models import {class_name}\n"
                "from modkit import get_db\n\n"
                "router = APIRouter()\n\n"
                f"@router.post('/{table_name}')\n"
                f"def create_item(item: {class_name}, db: Session = Depends(get_db)):\n"
                "    db.add(item)\n"
                "    db.commit()\n"
                "    db.refresh(item)\n"
                "    return item\n\n"
                f"@router.get('/{table_name}')\n"
                "def get_items(db: Session = Depends(get_db)):\n"
                f"    return db.query({class_name}).all()\n\n"
                f"@router.get('/{table_name}" + "/{item_id}')\n"
                "def get_item(item_id: int, db: Session = Depends(get_db)):\n"
                f"    item = db.query({class_name}).get(item_id)\n"
                "    if not item:\n"
                "        raise HTTPException(status_code=404, detail='Item not found')\n"
                "    return item\n\n"
                f"@router.put('/{table_name}" + "/{item_id}')\n"
                f"def update_item(item_id: int, update: {class_name}, db: Session = Depends(get_db)):\n"
                f"    item = db.query({class_name}).get(item_id)\n"
                "    if not item:\n"
                "        raise HTTPException(status_code=404, detail='Item not found')\n"
                "    for key, value in vars(update).items():\n"
                "        if key != '_sa_instance_state':\n"
                "            setattr(item, key, value)\n"
                "    db.commit()\n"
                "    return item\n\n"
                f"@router.delete('/{table_name}" + "/{item_id}')\n"
                "def delete_item(item_id: int, db: Session = Depends(get_db)):\n"
                f"    item = db.query({class_name}).get(item_id)\n"
                "    if not item:\n"
                "        raise HTTPException(status_code=404, detail='Item not found')\n"
                "    db.delete(item)\n"
                "    db.commit()\n"
                "    return {'deleted': True}\n"
            )

    print("✅ Done!")
