# Use the official Python image with a slim base
FROM python:3.11-slim

# Set a working directory for the application
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code to the working directory
COPY . /app/

# Expose port 8000 for the application
EXPOSE 8000

# Set the entry point for the application
CMD ["gunicorn", "healthapi.wsgi:application", "--bind", "0.0.0.0:8000"]
