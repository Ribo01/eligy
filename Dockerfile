FROM python:3

# Set the working directory to /app
WORKDIR /app

# Installing pip module for use in project
RUN pip install requests

# Copy the current directory contents into the container at /app
ADD . /app

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
