from langflow.utils.version import get_version_info

def build_label() -> str:
    info = get_version_info()
    v = info.get('version', 'unknown') if isinstance(info, dict) else str(info)
    return f'langflow-{v}'

def is_release() -> bool:
    return 'dev' not in build_label()
