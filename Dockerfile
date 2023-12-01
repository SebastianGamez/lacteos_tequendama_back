# Description: Dockerfile for building a docker image for the application
# Author: Sebastián Gámez Ariza

# Base image
FROM python:3.11-bullseye

# Stablish the working directory
WORKDIR /code

# Copy the requirements file
COPY ./requirements.txt /code/requirements.txt

# Install the requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application
COPY . /code

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


