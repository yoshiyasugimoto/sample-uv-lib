def greet(name: str = "World") -> str:
    """Greet someone with a personalized message."""
    return f"Hello, {name}! Welcome to mylib!"


def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


def get_library_info() -> dict:
    """Get information about the library."""
    return {
        "name": "mylib",
        "version": "0.1.0",
        "description": "A sample library created with uv"
    }