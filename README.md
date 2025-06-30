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
├── compose.yml             # Docker Compose configuration
├── api/                    # FastAPI application package (main project)
│   ├── __init__.py         # Package marker
│   ├── main.py             # FastAPI application
│   ├── pyproject.toml      # Main project configuration
│   ├── uv.lock             # Dependency lock file
│   └── Dockerfile          # Docker container configuration
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

2. **Navigate to the API directory:**
   ```bash
   cd api
   ```

3. **Install dependencies:**
   ```bash
   # Production dependencies only
   uv sync
   
   # Include development dependencies
   uv sync --dev
   ```

4. **Run the application:**
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
# Navigate to api directory
cd api

# Install dev dependencies first
uv sync --dev

# Lint and auto-fix
uv run ruff check --fix

# Format code
uv run ruff format
```

### Adding Dependencies

```bash
# Navigate to api directory first
cd api

# Add runtime dependency
uv add package-name

# Add development dependency
uv add --dev package-name
```

### Testing

```bash
# Navigate to api directory first
cd api

# Run tests (when implemented)
uv run pytest
```

## Configuration

### Environment Variables

- `PYTHONDONTWRITEBYTECODE=1` - Prevent Python from writing pyc files
- `PYTHONUNBUFFERED=1` - Force stdout and stderr to be unbuffered

### Project Management

This project manages dependencies at the `api/` level:

- **api/**: Main FastAPI application with its own `pyproject.toml` and `uv.lock`
- **mylib/**: Local utility library included as a path dependency
- Dependencies are managed in `api/pyproject.toml`
- All UV commands should be run from the `api/` directory

## Docker

### Build Arguments

None currently defined.

### Volumes

For production deployment, no volumes are mounted to ensure consistent runtime environment.

### Ports

- `8000` - FastAPI application

## Contributing

1. Navigate to api directory: `cd api`
2. Install development dependencies: `uv sync --dev`
3. Make your changes
4. Run code quality checks: `uv run ruff check --fix && uv run ruff format`
5. Test your changes: `docker compose up --build`

## License

This is a sample project for demonstration purposes.