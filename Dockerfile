# Dockerfile
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Use Django's dev server for now
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
