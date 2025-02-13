from src.data_loader import DataLoader
from src.model_trainer import ModelTrainer
from src.model_evaluator import ModelEvaluator
from src.digit_predictor import DigitPredictor
from src.visualizer import Visualizer


# Step 1: Load Data
loader = DataLoader()
(x_train, y_train), (x_test, y_test) = loader.load_data()

# Step 2: Train Model
trainer = ModelTrainer(x_train, y_train, x_test, y_test)
history = trainer.train(epochs=5)

# Step 3: Evaluate Model
evaluator = ModelEvaluator(x_test, y_test)
evaluator.evaluate()

# Step 4: Visualizations
visualizer = Visualizer()
visualizer.plot_training_history(history)

# Show MNIST sample images
visualizer.plot_sample_images(x_train, y_train)

# Show training accuracy & loss history
visualizer.plot_training_history(history)

# Show confusion matrix
visualizer.plot_confusion_matrix(x_test, y_test)

# Step 5: Test Prediction on a New Image (Replace "digit.png" with your image path)
visualizer.visualize_prediction("digit.png")
