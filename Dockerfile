# Use a lightweight official Python image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the necessary environment variables
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Collect the static files
RUN python manage.py collectstatic --noinput

# Expose the port the application will run on
EXPOSE 8000

# Start the application with Gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]