import tensorflow as tf
import numpy as np
from PIL import Image
import os
import json

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'waste_classification_model.h5')
CLASS_NAMES_PATH = os.path.join(BASE_DIR, 'class_names.json')

# Categories mapping with dynamic loading support
def _load_categories():
    """Load class names saved during training or fall back to defaults."""
    fallback = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
    if os.path.exists(CLASS_NAMES_PATH):
        try:
            with open(CLASS_NAMES_PATH, 'r', encoding='utf-8') as f:
                loaded = json.load(f)
            if isinstance(loaded, list) and all(isinstance(item, str) for item in loaded):
                return loaded
            print(f"Warning: {CLASS_NAMES_PATH} is not a list of strings. Falling back to defaults.")
        except Exception as exc:
            print(f"Warning: Failed to read {CLASS_NAMES_PATH}: {exc}. Falling back to defaults.")
    else:
        print(f"Warning: {CLASS_NAMES_PATH} not found. Using default class labels.")
    return fallback

CATEGORIES = _load_categories()

# Global variable to store the model (loaded lazily)
model = None

def load_model():
    """Load the model lazily when needed."""
    global model
    if model is None:
        print(f"Attempting to load model from: {MODEL_PATH}")
        
        # Check if file exists
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}. Please check if the file exists at this location.")
        
        try:
            model = tf.keras.models.load_model(MODEL_PATH)
            print("Model loaded successfully!")
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise
    return model

def preprocess_image(image_path):
    """Preprocess the image to match model requirements."""
    # Load and resize image
    img = Image.open(image_path)
    img = img.resize((128, 128))
    
    # Convert to array and preprocess
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    img_array = img_array / 255.0  # Normalize
    
    return img_array

def predict_waste_category(image_path):
    """Predict the waste category for a given image."""
    # Load model if not already loaded
    model = load_model()
    
    # Preprocess the image
    processed_image = preprocess_image(image_path)
    
    # Make prediction
    predictions = model.predict(processed_image)
    predicted_class = np.argmax(predictions[0])
    
    # Return predicted category
    try:
        return CATEGORIES[predicted_class]
    except IndexError:
        raise ValueError(
            f"Predicted class index {predicted_class} is out of range for categories list of length {len(CATEGORIES)}."
        )