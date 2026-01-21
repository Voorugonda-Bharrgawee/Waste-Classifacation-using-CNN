# 🚀 How to Run This Code in VS Code

This guide will walk you through running the Waste Classification Flask application in Visual Studio Code.

## 📋 Prerequisites

- ✅ Python 3.10+ installed
- ✅ Visual Studio Code installed
- ✅ VS Code Python extension installed

## 🎯 Step-by-Step Setup

### Step 1: Open the Project in VS Code

1. Open **Visual Studio Code**
2. Click **File** → **Open Folder**
3. Navigate to: `D:\PROJECT\waste-classification-main\waste-classification-main`
4. Click **Select Folder**

### Step 2: Select Python Interpreter

1. Press `Ctrl + Shift + P` to open the command palette
2. Type: `Python: Select Interpreter`
3. Choose one of these options:
   - **Option A**: Select the virtual environment (if it exists):
     - `.\venv\Scripts\python.exe`
   - **Option B**: Select your system Python (if venv doesn't exist yet)

### Step 3: Activate/Create Virtual Environment

**If virtual environment already exists:**
- VS Code should detect it automatically
- If not, select it manually (see Step 2)

**If you need to create a new virtual environment:**

1. Open the integrated terminal in VS Code:
   - Press `` Ctrl + ` `` (backtick) or
   - Go to **Terminal** → **New Terminal**

2. Run these commands:
   ```powershell
   cd D:\PROJECT\waste-classification-main\waste-classification-main
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

### Step 4: Install Dependencies

In the VS Code terminal (make sure venv is activated), run:

```powershell
pip install -r requirements.txt
```

This will install:
- Flask
- TensorFlow
- Pillow
- NumPy

### Step 5: Check if Model Exists

Before running the app, check if you have the trained model:

- **Model file should be at**: `waste_classification_model.h5`
- **If the model doesn't exist**, you'll need to train it first (see Step 6)

### Step 6: Train the Model (If Needed)

If `waste_classification_model.h5` doesn't exist:

1. Make sure your dataset is at: `D:\PROJECT\dataset-resized`
2. In the VS Code terminal, run:
   ```powershell
   python train_model.py
   ```
3. Wait for training to complete (30-60 minutes)
4. The model will be saved automatically

### Step 7: Run the Flask Application

**Method 1: Using VS Code Terminal**

1. Open the terminal in VS Code (`` Ctrl + ` ``)
2. Make sure your virtual environment is activated (you should see `(venv)` in the prompt)
3. Run:
   ```powershell
   python app.py
   ```

**Method 2: Using VS Code Run Configuration**

1. Click the **Run and Debug** icon in the sidebar (or press `Ctrl + Shift + D`)
2. Click **create a launch.json file**
3. Select **Python: Flask**
4. VS Code will create a configuration file
5. Press `F5` to start debugging, or click the green play button

**Method 3: Using the Play Button**

1. Open `app.py` in VS Code
2. Click the green **▶ Run** button at the top right
3. Select **Python File** when prompted

### Step 8: Access the Application

Once the Flask app is running, you'll see output like:
```
 * Running on http://127.0.0.1:5000
 * Running on http://localhost:5000
```

1. Open your web browser
2. Navigate to: **http://localhost:5000**
3. Upload an image to test the classification!

## 🎨 VS Code Tips

### Debugging

1. Set breakpoints by clicking in the left margin next to line numbers
2. Press `F5` to start debugging
3. Use the debug toolbar to step through code

### Terminal Shortcuts

- `` Ctrl + ` `` - Toggle terminal
- `Ctrl + Shift + `` - Create new terminal
- `Ctrl + K` then `Ctrl + U` - Clear terminal

### Python Extension Features

- **IntelliSense**: Auto-completion for Python code
- **Linting**: Automatic error detection
- **Formatting**: Right-click → **Format Document**

## 🔧 Troubleshooting

### Issue: "Python is not recognized"

**Solution:**
- Make sure Python is installed and added to PATH
- Or use: `py app.py` instead of `python app.py`

### Issue: "Module not found"

**Solution:**
- Make sure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### Issue: "Model file not found"

**Solution:**
- Train the model first: `python train_model.py`
- Or place a pre-trained model file at: `waste_classification_model.h5`

### Issue: "Port 5000 already in use"

**Solution:**
- Close other applications using port 5000
- Or modify `app.py` to use a different port:
  ```python
  app.run(debug=True, port=5001)
  ```

### Issue: Virtual environment not activating in PowerShell

**Solution:**
Run this command first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📝 Quick Reference

| Task | Command |
|------|---------|
| Activate venv | `.\venv\Scripts\Activate.ps1` |
| Install dependencies | `pip install -r requirements.txt` |
| Train model | `python train_model.py` |
| Run Flask app | `python app.py` |
| Deactivate venv | `deactivate` |

## 🎯 Next Steps

1. ✅ Run the Flask app
2. ✅ Open http://localhost:5000 in your browser
3. ✅ Upload a waste image to test classification
4. ✅ Check the results!

---

**Happy Coding! 🚀**

