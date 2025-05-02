# Use official Python image as base
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy your code and dependencies into the container
COPY . /app

# Install dependencies inside the container
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run your app
CMD ["python", "app.py"]  # replace with your main file
