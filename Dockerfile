FROM python:3.11-slim

# Set a working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app/

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "healthapi.wsgi:application", "--bind", "0.0.0.0:8000"]
