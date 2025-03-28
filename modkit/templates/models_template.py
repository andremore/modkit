def render(class_name: str, table_name: str) -> str:
    return f"""from modkit import Base
from sqlalchemy import Column, Integer, String

class {class_name}(Base):
    __tablename__ = "{table_name}"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
"""
