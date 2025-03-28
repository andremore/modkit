def render(class_name: str, table_name: str) -> str:
    return f"""from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import {class_name}
from modkit import get_db

router = APIRouter()

@router.post("/{table_name}")
def create_item(item: {class_name}, db: Session = Depends(get_db)):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/{table_name}")
def get_items(db: Session = Depends(get_db)):
    return db.query({class_name}).all()

@router.get("/{table_name}/{{item_id}}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query({class_name}).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{table_name}/{{item_id}}")
def update_item(item_id: int, update: {class_name}, db: Session = Depends(get_db)):
    item = db.query({class_name}).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in vars(update).items():
        if key != "_sa_instance_state":
            setattr(item, key, value)
    db.commit()
    return item

@router.delete("/{table_name}/{{item_id}}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query({class_name}).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {{"deleted": True}}
"""
