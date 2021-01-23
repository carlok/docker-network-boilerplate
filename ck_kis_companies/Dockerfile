# Use Python 3.8
FROM python:3.8

# Set working directory
RUN mkdir /app
WORKDIR /app

# Add all files to app directory
ADD . /app

# Install gunicorn
RUN apt-get update && \
    apt-get install -y && \
    pip3 install gunicorn

# Run setup.py
RUN python3 setup.py install
