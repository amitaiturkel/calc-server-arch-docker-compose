# Stage 1: Build your Python application image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Pyproject.toml and poetry.lock files into the container
COPY . .

# Install Poetry and project dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Define the command to run your Python application
CMD ["python", "poetry_demo/calc_server.py", "--nats-port", "4222"]
