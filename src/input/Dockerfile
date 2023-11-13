# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock /app/

# Install pipenv and project dependencies
RUN pip install --no-cache-dir pipenv && \
    pipenv install --deploy --ignore-pipfile

# Copy the current directory contents into the container at /app
COPY . /app

# Environment variable
ENV FLASK_APP=file_input.py 

# Expose port 5000
EXPOSE 5000

# TODO: Fix http://172.17.0.2:5000/ serving
# Run the Flask app
CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]