from .main import greet, add_numbers, get_library_info

def hello() -> str:
    return "Hello from mylib!"

__all__ = ["hello", "greet", "add_numbers", "get_library_info"]