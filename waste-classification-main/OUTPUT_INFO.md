# Waste Classification App - Output Information

## Current Status

✅ **Flask Server**: Running on `http://localhost:5000`
✅ **Dependencies**: All installed (Flask, TensorFlow, Pillow, NumPy)
✅ **Code**: Fixed and ready
❌ **Model File**: Missing (`waste_classification_model.h5`)

## Expected Outputs

### 1. When You Access the Web Interface (`http://localhost:5000`)

**Home Page Output:**
- A web page with:
  - Title: "Waste Classification"
  - Upload area with drag-and-drop functionality
  - File input button
  - "Classify Waste" submit button

### 2. When You Upload an Image (WITH Model File)

**Success Output:**
```json
{
  "status": "success",
  "category": "glass"  // or: cardboard, metal, paper, plastic, trash
}
```

**Result Page Shows:**
- Uploaded image displayed
- Predicted category with icon
- "Classify Another Image" button

### 3. When You Upload an Image (WITHOUT Model File)

**Error Output:**
```json
{
  "error": "Model file not found. Please place the waste_classification_model.h5 file in the same directory as app.py and utils.py"
}
```

### 4. Console Output (When Model Loads Successfully)

```
Attempting to load model from: D:\PROJECT\waste-classification-main\waste-classification-main\waste_classification_model.h5
Model loaded successfully!
```

### 5. Console Output (When Prediction Runs)

```
Attempting to load model from: D:\PROJECT\waste-classification-main\waste-classification-main\waste_classification_model.h5
Model loaded successfully!
127.0.0.1 - - [12/Nov/2025 22:42:40] "POST /predict HTTP/1.1" 200 -
```

## Possible Categories

The model can classify waste into 6 categories:
1. **cardboard**
2. **glass**
3. **metal**
4. **paper**
5. **plastic**
6. **trash**

## How to Get the Model File

1. **Train the model** using `WASTE_MANAGEMENT.ipynb` notebook
2. **Download** a pre-trained model if available
3. **Place** the `waste_classification_model.h5` file in:
   ```
   D:\PROJECT\waste-classification-main\waste-classification-main\
   ```

## Testing the App

1. Open browser: `http://localhost:5000`
2. Upload an image (PNG, JPG, or JPEG)
3. Click "Classify Waste"
4. View the result (or error message if model is missing)







