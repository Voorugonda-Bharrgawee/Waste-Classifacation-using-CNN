import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, render_template, request, jsonify
import numpy as np
import os
import json
import io

# --- Model Files ---
MODEL_SAVE_PATH = 'waste_classification_model.h5'
CLASS_NAMES_PATH = 'class_names.json'
IMG_SIZE = (128, 128)

# Flask App
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Global vars
model = None
class_names = None

# --- Load Model ---
def load_local_model():
    global model, class_names

    if os.path.exists(MODEL_SAVE_PATH) and os.path.exists(CLASS_NAMES_PATH):
        try:
            print("Loading model...")
            model = load_model(MODEL_SAVE_PATH, compile=False)

            with open(CLASS_NAMES_PATH, 'r') as f:
                class_names = json.load(f)

            print("Model loaded successfully!")
            return True
        except Exception as e:
            print(f"ERROR loading model: {e}")
            return False
    else:
        print("Model or class_names.json not found!")
        return False


# --- Prediction Logic ---
def classify_image_locally(img_file):
    global model, class_names

    if model is None or class_names is None:
        return "Model Not Loaded", 0.0

    # Read stream correctly
    img_file.stream.seek(0)
    image_bytes = io.BytesIO(img_file.stream.read())

    # Preprocess
    img = image.load_img(image_bytes, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Predict
    predictions = model.predict(img_array)
    score = float(np.max(predictions))
    predicted_index = int(np.argmax(predictions))
    predicted_name = class_names[predicted_index]

    return predicted_name, score


# --- Helpers ---
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# --- Routes ---
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        category, confidence = classify_image_locally(file)

        if category == "Model Not Loaded":
            return jsonify({'error': "Model not loaded. Check server logs."}), 500

        # Save uploaded file
        file.stream.seek(0)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(save_path)

        # ✅ Only this was changed
        return render_template(
            'result.html',
            filename=file.filename,
            category=category,
            confidence=f"{confidence*100:.2f}%"
        )

    return jsonify({'error': 'Invalid file type'}), 400


# --- Run App ---
if __name__ == '__main__':
    load_local_model()

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    app.run(debug=True)
