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

# Use a non-root user to run the application
USER nobody

# Command to run the application
CMD ["gunicorn", "healthapi.wsgi:application", "--bind", "0.0.0.0:8000"]
