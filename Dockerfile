# Use Python 3.12.3 on Debian Bullseye base image
FROM python:3.12.3-bullseye

# Set working directory within the container
WORKDIR /app

# Copy all files from the current directory to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for FastAPI application
EXPOSE 80

# Command to run the FastAPI application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
