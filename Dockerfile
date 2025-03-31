FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get upgrade -y

# Create a working directory
WORKDIR /app

# Copy your script and utils directory
COPY . /app

# Default command
ENTRYPOINT ["python", "main.py"]
