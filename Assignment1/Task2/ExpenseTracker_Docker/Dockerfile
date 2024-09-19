# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install pip requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create uploads directory and set permissions for /app
RUN mkdir -p uploads && chmod -R 777 /app

# Switch to non-root user
USER nobody

EXPOSE 5001

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "app.py"]