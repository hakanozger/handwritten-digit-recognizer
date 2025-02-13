from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import cv2
import os

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Requests

# Get the absolute path to the model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "mnist_model.h5")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Model file not found at {MODEL_PATH}! Please train the model first.")


model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_image(image_path):
    """Preprocess the image for model prediction."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (28, 28))  # Resize to 28x28
    image = image / 255.0  # Normalize
    image = image.reshape(1, 28, 28, 1)  # Reshape for CNN
    return image

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Handwritten Digit Recognizer API!"})

@app.route("/predict", methods=["POST"])
def predict():
    """Predicts the digit from an uploaded image."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    # Ensure the upload directory exists
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, "uploaded_image.png")
    file.save(file_path)

    # Preprocess the image
    processed_image = preprocess_image(file_path)

    # Predict
    prediction = np.argmax(model.predict(processed_image))

    # Delete the temporary image
    os.remove(file_path)

    return jsonify({"predicted_digit": int(prediction)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
