# How to Get the Model File

## Quick Summary

Your Flask app is **running** at `http://localhost:5000`, but you need the model file to make predictions.

## Option 1: Train the Model (Recommended if you have the dataset)

1. **Open the Jupyter Notebook:**
   ```
   WASTE_MANAGEMENT.ipynb
   ```

2. **Update the dataset path** in the notebook:
   - Change line 36 from: `data_dir = '/Users/tanishq/Desktop/dataset-resized'`
   - To: `data_dir = 'D:/PROJECT/dataset-resized'` (or your actual path)

3. **Update the model save path** in the notebook:
   - Change line 286 from: `model.save('/Users/tanishq/Desktop/untitled folder/waste_classification_model.h5')`
   - To: `model.save('waste_classification_model.h5')` (saves in current directory)

4. **Run all cells** in the notebook to train the model

5. **The model will be saved** as `waste_classification_model.h5` in the same folder

## Option 2: Use a Pre-trained Model

If you have a pre-trained model file:
1. Place it in: `D:\PROJECT\waste-classification-main\waste-classification-main\`
2. Name it: `waste_classification_model.h5`

## Current Status

✅ Flask server: Running on port 5000  
✅ Dependencies: Installed  
✅ Code: Fixed and ready  
❌ Model file: Missing

## Test the App

1. Open browser: `http://localhost:5000`
2. Upload an image
3. You'll see either:
   - **Success**: Classification result (if model exists)
   - **Error**: "Model file not found" message (currently)

## Expected Output When Working

**Success Response:**
- Web page showing:
  - Your uploaded image
  - Predicted category: `cardboard`, `glass`, `metal`, `paper`, `plastic`, or `trash`

**Console Output:**
```
Attempting to load model from: D:\PROJECT\waste-classification-main\waste-classification-main\waste_classification_model.h5
Model loaded successfully!
```







