# How to Run the Training Script

## Method 1: Double-Click (Easiest) ⭐

1. Navigate to: `D:\PROJECT\waste-classification-main\waste-classification-main\`
2. Double-click: `RUN_TRAINING.bat`
3. Wait for training to complete (30-60 minutes)

## Method 2: PowerShell/Command Prompt

1. **Open PowerShell** (Right-click Start → Windows PowerShell) or **Command Prompt**

2. **Copy and paste these commands one by one:**

```powershell
cd D:\PROJECT\waste-classification-main\waste-classification-main
python train_model.py
```

3. **Press Enter** after each command

## Method 3: From Current Directory

If you're already in the project directory, just run:

```powershell
python train_model.py
```

## What You'll See

The script will:
1. ✅ Check if dataset exists
2. ✅ Load training and validation data
3. ✅ Build the model
4. ✅ Start training (you'll see progress for each epoch)
5. ✅ Save the model automatically when done

## Expected Output

```
Dataset directory: D:\PROJECT\dataset-resized
Model will be saved to: D:\PROJECT\waste-classification-main\waste-classification-main\waste_classification_model.h5

Loading training data...
Found 2024 images belonging to 6 classes.
Loading validation data...
Found 503 images belonging to 6 classes.

Computing class weights...
Building model...
Model compiled successfully!

Starting training...
Epoch 1/50
...
```

## After Training Completes

1. The model will be saved automatically
2. Restart your Flask app (if it's running)
3. Try uploading an image - it should work now!

## Troubleshooting

**If you get "python is not recognized":**
- Use: `py train_model.py` instead of `python train_model.py`

**If training is too slow:**
- This is normal - training takes 30-60 minutes
- You can reduce epochs in the script if needed

**If you get an error about the dataset:**
- Make sure `D:\PROJECT\dataset-resized` exists
- Check that it contains folders: cardboard, glass, metal, paper, plastic, trash







