# Use Python 3.10 Alpine as the base image
FROM python:3.10-alpine

# Set environment variables for non-interactive installations
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies needed for GDAL, PostGIS, GEOS, and other libraries
RUN apk update && apk add --no-cache \
    build-base \
    postgresql-dev \
    postgis \
    gdal \
    gdal-dev \
    libjpeg-turbo-dev \
    zlib-dev \
    libffi-dev \
    python3-dev \
    musl-dev \
    bash \
    geos-dev  # Install GEOS development libraries for shapely

# Install pipenv for managing the virtual environment
RUN pip install pipenv

# Set the working directory inside the container
WORKDIR /waste_management_app

# Copy the Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock /waste_management_app/

# Install project dependencies in the virtual environment using pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code into the container
COPY . /waste_management_app/

# Set environment variable to run the Django server on any host
ENV PYTHONUNBUFFERED 1

# Expose the port the app will run on
EXPOSE 8000

# Run the Django development server (you can replace this with Gunicorn for production)
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
