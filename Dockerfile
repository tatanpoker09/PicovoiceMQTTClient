# Use an official Python runtime as a parent image
FROM python:3.11-bookworm
RUN apt update
RUN apt install -y alsa-base alsa-utils

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "script.py"]
