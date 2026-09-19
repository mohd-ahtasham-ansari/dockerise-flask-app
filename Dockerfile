# base image
FROM python:3.11-slim

# choose work directory
WORKDIR /app

# copy requirements.txt file
COPY requirements.txt .
# run command
RUN pip install --no-cache-dir -r requirements.txt

# copy command
COPY . /app

# port 
EXPOSE 5000

# command
CMD ["python", "./app.py"]