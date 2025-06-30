# Use an official Python 3.13 image
FROM python:3.13-slim

# Set environment variables
ENV POETRY_VERSION=2.1.3 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install Poetry
RUN pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION"

WORKDIR /app

# Copy only the necessary files for Poetry to install dependencies
COPY pyproject.toml poetry.lock* /app/

# Install dependencies (no virtualenvs)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Run the application with Uvicorn
CMD ["poetry", "run", "uvicorn", "src.main.main:app", "--host", "0.0.0.0", "--port", "8000"]