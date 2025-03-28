from .types import ModuleContract

class ModuleBuilder:
    def __init__(self):
        self._contract: ModuleContract = {}

    def add_model(self, model):
        self._contract.setdefault("models", []).append(model)
        return self

    def add_router(self, router, prefix: str = ""):
        router.prefix = prefix
        self._contract.setdefault("routers", []).append(router)
        return self

    def add_event(self, event):
        self._contract.setdefault("events", []).append(event)
        return self

    def add_task(self, task):
        self._contract.setdefault("tasks", []).append(task)
        return self

    def with_context(self, key: str, value: object):
        self._contract.setdefault("context", {})[key] = value
        return self

    def build(self) -> ModuleContract:
        return self._contract
