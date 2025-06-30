# Sample UV Library

A sample Python project demonstrating UV package manager integration with Docker and FastAPI.

## Features

- **Python 3.13** with UV package manager
- **Docker** containerization with optimized builds
- **FastAPI** web framework
- **Workspace** setup with local `mylib` package
- **Ruff** for linting and formatting (replaces black + isort)

## Project Structure

```
├── Dockerfile              # Docker container configuration
├── compose.yml             # Docker Compose configuration
├── main.py                 # FastAPI application
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Dependency lock file
├── mylib/                  # Local library package
│   ├── src/mylib/
│   │   ├── __init__.py     # Package exports
│   │   ├── main.py         # Core library functions
│   │   └── py.typed        # Type hints marker
│   ├── pyproject.toml      # Library configuration
│   └── README.md           # Library documentation
└── README.md               # This file
```

## Quick Start

### Using Docker Compose (Recommended)

1. **Start the application:**
   ```bash
   docker compose up --build
   ```

2. **Access the API:**
   - Main endpoint: http://localhost:8000/
   - Health check: http://localhost:8000/health
   - API documentation: http://localhost:8000/docs

3. **Stop the application:**
   ```bash
   docker compose down
   ```

### Local Development

1. **Install UV:**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install dependencies:**
   ```bash
   # Production dependencies only
   uv sync
   
   # Include development dependencies
   uv sync --dev
   ```

3. **Run the application:**
   ```bash
   uv run uvicorn main:app --reload
   ```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Hello message from mylib |
| `/health` | GET | Health check |
| `/info` | GET | Library information |
| `/greet/{name}` | GET | Personalized greeting |
| `/add/{a}/{b}` | GET | Add two numbers |

### Example Usage

```bash
# Get hello message
curl http://localhost:8000/

# Health check
curl http://localhost:8000/health

# Greet a user
curl http://localhost:8000/greet/Alice

# Add numbers
curl http://localhost:8000/add/5/3
```

## Development

### Code Quality

The project uses **Ruff** for both linting and formatting.

**Local Development:**
```bash
# Install dev dependencies first
uv sync --dev

# Lint and auto-fix
uv run ruff check --fix

# Format code
uv run ruff format
```

**Docker Container:**
```bash
# Development dependencies are not included in production container
# For linting in Docker, rebuild with dev dependencies:
docker run --rm -v $(pwd):/app -w /app python:3.13-slim sh -c "pip install uv && uv sync --dev && uv run ruff check ."
```

### Adding Dependencies

```bash
# Add runtime dependency
uv add package-name

# Add development dependency
uv add --dev package-name
```

### Testing

```bash
# Run tests (when implemented)
uv run pytest
```

## Configuration

### Environment Variables

- `PYTHONDONTWRITEBYTECODE=1` - Prevent Python from writing pyc files
- `PYTHONUNBUFFERED=1` - Force stdout and stderr to be unbuffered

### UV Workspace

This project uses UV's workspace feature to manage the local `mylib` package:

- Workspace members are defined in `pyproject.toml`
- Local dependencies are specified in `tool.uv.sources`
- Both packages are built and installed together

## Docker

### Build Arguments

None currently defined.

### Volumes

- `./:/app` - Mount source code for development

### Ports

- `8000` - FastAPI application

## Contributing

1. Install development dependencies: `uv sync --dev`
2. Make your changes
3. Run code quality checks: `uv run ruff check --fix && uv run ruff format`
4. Test your changes: `docker compose up --build`

## License

This is a sample project for demonstration purposes.