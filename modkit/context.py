_context: dict[str, object] = {}

def register_in_context(key: str, value: object) -> None:
    _context[key] = value

def get_from_context(key: str) -> object:
    return _context.get(key)
