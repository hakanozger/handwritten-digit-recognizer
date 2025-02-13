# Handwritten Digit Recognizer

## Overview
This project is a **handwritten digit recognition system** built using **Flask (backend) and React (frontend)**. It uses a **Convolutional Neural Network (CNN) trained on the MNIST dataset** to classify handwritten digits (0-9). The system is containerized with **Docker and Docker Compose**, making it easy to deploy with a single command.

## Features
- 🧠 **Deep Learning Model** - Uses an improved CNN model trained on the MNIST dataset.
- 📸 **Image Upload Support** - Users can upload handwritten digit images for recognition.
- 🌐 **Web Interface** - Built with React for an interactive UI.
- 🚀 **REST API** - Flask backend exposes an API for image classification.
- 📦 **Containerized with Docker** - Runs seamlessly with **Docker Compose**.
- 🎯 **Data Augmentation** - Enhances model accuracy on real-world images.

---

## Project Structure
```
handwritten-digit-recognizer/
│── backend/                         # Flask API & Model
│   ├── flask_api.py                 # Flask API for predictions
│   ├── model_trainer.py             # Train the MNIST model (runs inside container)
│   ├── model/                        # Model directory
│   │   ├── mnist_model.h5            # Trained model
│   ├── uploads/                      # Stores uploaded images
│   ├── requirements.txt              # Python dependencies
│   ├── Dockerfile                    # Docker config for Flask & Model Training
│── frontend/                         # React UI
│   ├── src/
│   │   ├── App.js                    # Main React component
│   │   ├── ImageUploader.js           # Image Upload Component
│   │   ├── index.js                   # React Entry Point
│   │   ├── styles.css                 # Styling
│   ├── public/
│   │   ├── index.html                 # Main HTML file
│   ├── package.json                   # React dependencies
│   ├── Dockerfile                      # Docker config for React
│── docker-compose.yml                  # Docker Compose for multi-container setup
│── README.md                           # Project Documentation
```

---

## Installation & Setup

### **1️⃣ Prerequisites**
Make sure you have:
- **Docker** installed → [Install Docker](https://docs.docker.com/get-docker/)
- **Node.js & npm** (for frontend development) → [Download Node.js](https://nodejs.org/)

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/handwritten-digit-recognizer.git
cd handwritten-digit-recognizer
```

### **3️⃣ Build and Start the Containers**
```bash
docker compose up --build
```
This will:
✅ **Train the model (if not already trained)**
✅ **Start the Flask API** on `http://localhost:5001`
✅ **Start the React UI** on `http://localhost:3000`

### **4️⃣ Stop the Containers**
To stop all running services:
```bash
docker compose down
```

---

## API Endpoints
### **1️⃣ Check API Status**
```bash
GET http://localhost:5001/
```
**Response:**
```json
{ "message": "Welcome to the Handwritten Digit Recognizer API!" }
```

### **2️⃣ Predict a Digit**
Upload a handwritten digit image:
```bash
curl -X POST -F "file=@digit.png" http://localhost:5001/predict
```
**Response:**
```json
{ "predicted_digit": 3 }
```

---

## Web Interface (React Frontend)
Once running, visit:
```
http://localhost:3000
```
✅ Upload an image of a handwritten digit
✅ Click **Predict** to get the result
✅ View the predicted digit instantly

---

## Model Training
The model is trained using an **improved CNN** with **data augmentation** to handle real-world handwriting variations.

### **Training Script** (`backend/model_trainer.py`)
- Uses **three convolutional layers** with **Batch Normalization**
- **Dropout layers** added to prevent overfitting
- **Data Augmentation** (rotation, zoom, shift) applied
- Trained using the **MNIST dataset**

To manually re-train the model:
```bash
docker compose run backend python model_trainer.py
```
This will re-train and save the model to:
```
backend/model/mnist_model.h5
```

---

## Deployment
Want to deploy this project?

### **1️⃣ Deploy with Docker on a Remote Server**
On your **remote server (AWS, GCP, DigitalOcean, etc.)**:
```bash
git clone https://github.com/your-repo/handwritten-digit-recognizer.git
cd handwritten-digit-recognizer
docker compose up --build -d
```

### **2️⃣ Deploy to Render, Vercel, or Heroku**
- **Backend:** Use Render, AWS Lambda, or Heroku for Flask API
- **Frontend:** Use Vercel or Netlify for React UI

---

## Troubleshooting
### **1️⃣ Flask API Not Starting?**
Check if model exists:
```bash
ls backend/model/
```
If missing, re-train it:
```bash
docker compose run backend python model_trainer.py
```

### **2️⃣ React App Not Loading?**
Try clearing cache:
```bash
cd frontend
rm -rf node_modules package-lock.json
docker compose up --build
```

---

## License
This project is licensed under the **MIT License**.

---

## 👨‍💻 Contributing
Got improvements? Feel free to fork and submit a PR!
```bash
git clone https://github.com/your-repo/handwritten-digit-recognizer.git
cd handwritten-digit-recognizer
```

---

## 🌟 Credits
Built by Hakan Özger 🚀

