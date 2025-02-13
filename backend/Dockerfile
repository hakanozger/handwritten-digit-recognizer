# Use official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (fixes OpenCV issue)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Copy the Flask app files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the uploads directory exists
RUN mkdir -p uploads model

# Train the model before starting Flask API
RUN python model_trainer.py

# Expose port 5001 for Flask API
EXPOSE 5001

# Run the Flask API
CMD ["python", "flask_api.py"]
