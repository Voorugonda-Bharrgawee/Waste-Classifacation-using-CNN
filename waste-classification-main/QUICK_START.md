# Quick Start Guide - Fix the Model Error

## The Problem
You're getting this error:
```json
{
  "error": "Model file not found at: D:\\PROJECT\\waste-classification-main\\waste-classification-main\\waste_classification_model.h5"
}
```

## The Solution

You have **2 options**:

### Option 1: Train the Model (Recommended)

I've created a training script for you. Here's how to use it:

1. **The script is ready**: `train_model.py` is already configured with your dataset path
2. **Run the training**:
   ```bash
   cd D:\PROJECT\waste-classification-main\waste-classification-main
   python train_model.py
   ```
3. **Wait for training to complete** (this may take 30-60 minutes depending on your system)
4. **The model will be saved** automatically to the correct location
5. **Restart your Flask app** and try uploading an image again

### Option 2: Use a Pre-trained Model

If you have a pre-trained model file:
1. Place it in: `D:\PROJECT\waste-classification-main\waste-classification-main\`
2. Name it: `waste_classification_model.h5`
3. Restart your Flask app

## Current Status

✅ Dataset found at: `D:\PROJECT\dataset-resized`  
✅ Training script created: `train_model.py`  
✅ All dependencies installed  
✅ Flask app running on `http://localhost:5000`  
❌ Model file missing (needs to be trained or provided)

## After Training

Once the model is trained and saved, your Flask app will automatically:
- Load the model when you upload an image
- Classify the waste into one of 6 categories:
  - cardboard
  - glass
  - metal
  - paper
  - plastic
  - trash

## Note

Training the model will take time (30-60 minutes). The script will show progress and save the model automatically when done.







