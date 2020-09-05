# https://hub.docker.com/u/rocker
FROM rocker/tidyverse:3.6.2

# install python3
RUN apt-get update && apt-get install -y python3 python3-pip

# install the forecast package. from the littler package
RUN install2.r forecast

# Make dir in Docker
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app

# Copy R script to binaries directory
COPY r/script.R /usr/bin/script.R

# Run main.py when the container launches
CMD ["python3", "main.py"]
