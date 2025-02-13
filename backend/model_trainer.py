import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

MODEL_PATH = "backend/model/mnist_model.h5"

def build_and_train_model():
    """Builds and trains an improved CNN model for handwritten digit recognition."""

    if os.path.exists(MODEL_PATH):
        print(f"✅ Model already exists at {MODEL_PATH}. Skipping training.")
        return

    print("🚀 Training new model with data augmentation and improved CNN...")

    # Load MNIST dataset
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Normalize pixel values to [0,1]
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Reshape for CNN input
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)

    # Data Augmentation: Introduce distortions to mimic real handwriting
    datagen = ImageDataGenerator(
        rotation_range=10,  # Rotate images up to 10 degrees
        zoom_range=0.1,  # Zoom in randomly
        width_shift_range=0.1,  # Shift width
        height_shift_range=0.1  # Shift height
    )
    datagen.fit(x_train)

    # Build Improved CNN Model
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        layers.BatchNormalization(),  # Normalize activations
        layers.MaxPooling2D((2, 2)),

        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),

        layers.Conv2D(128, (3, 3), activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),

        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dropout(0.3),  # Reduce overfitting
        layers.Dense(64, activation="relu"),
        layers.Dropout(0.3),  
        layers.Dense(10, activation="softmax")
    ])

    # Compile model
    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    # Train model with data augmentation
    model.fit(datagen.flow(x_train, y_train, batch_size=32),
              validation_data=(x_test, y_test),
              epochs=10)

    # Ensure model directory exists
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    # Save model
    model.save(MODEL_PATH)
    print(f"✅ Improved model trained and saved to {MODEL_PATH}")

if __name__ == "__main__":
    build_and_train_model()
