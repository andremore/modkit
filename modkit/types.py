from fastapi import FastAPI
from typing import Any, TypedDict

AppType = FastAPI

class ModuleContract(TypedDict, total=False):
    models: list[Any]
    routers: list[Any]
    events: list[Any]
    tasks: list[Any]
    context: dict[str, Any]
