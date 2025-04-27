FROM python:3.12-slim

# Install system dependencies for OpenCV
RUN apt update && apt install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose port
EXPOSE 8000

# Start server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
