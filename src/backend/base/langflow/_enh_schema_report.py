from langflow.io import schema as _schema

def module_symbols() -> int:
    return len([n for n in dir(_schema) if not n.startswith('_')])

def has_symbol(name: str) -> bool:
    return hasattr(_schema, name)
