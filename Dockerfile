# Use an official Python runtime as a parent image
FROM python:3.13-alpine

# Set environment variables
# 1. Prevents Python from buffering stdout and stderr
# 2. Sets the working directory in the container
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using gunicorn
# We use gunicorn as it is a production-ready WSGI server
# The command runs migrations first and then starts the server.
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --no-input && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]