# Use Python 3.13 slim image as base
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Set work directory
WORKDIR /app

# Copy mylib dependency first
COPY ./mylib/ ./mylib/

# Copy api project files
COPY ./api/ .

# Update pyproject.toml to use correct mylib path in container
RUN sed -i 's|path = "../mylib"|path = "./mylib"|' pyproject.toml

# Install dependencies using uv (regenerate lock with new paths)
RUN uv sync

# Create non-root user
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Expose port
EXPOSE 8000

# Add .venv/bin to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Run the application directly with python
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]