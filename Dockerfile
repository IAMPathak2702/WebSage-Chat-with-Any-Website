# Use the latest Python 3.12 image as the base image
FROM python:3.12.3-bullseye

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Copy the entire project into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/src/requirements.txt

# Expose the port on which the FastAPI application will run (change if needed)
EXPOSE 8000

# Set the environment variables
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Set the working directory to the source code
WORKDIR /app/src

# Set the command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
