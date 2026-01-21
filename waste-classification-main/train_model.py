"""
Training script for Waste Classification Model
Run this script to train and save the model in the correct location.
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.utils.class_weight import compute_class_weight
import numpy as np
import os
import json

# Step 1: Define paths and parameters
# Change this to your dataset-resized folder
data_dir = r"C:\Users\nandi\OneDrive\Desktop\PROJECT\archive\dataset-resized"

img_size = (128, 128)
batch_size = 32

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_SAVE_PATH = os.path.join(BASE_DIR, 'waste_classification_model.h5')
CLASS_NAMES_PATH = os.path.join(BASE_DIR, 'class_names.json')


def _directory_has_images(path, extensions=None):
    """Return True if the directory (recursively) contains image files."""
    if extensions is None:
        extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}

    if not os.path.isdir(path):
        return False

    for root, _, files in os.walk(path):
        for file_name in files:
            if os.path.splitext(file_name)[1].lower() in extensions:
                return True
    return False


print(f"Dataset directory: {data_dir}")
print(f"Model will be saved to: {MODEL_SAVE_PATH}")

# Check if dataset exists
if not os.path.exists(data_dir):
    print(f"\nERROR: Dataset directory not found at: {data_dir}")
    print("Please update 'data_dir' to point to your dataset-resized folder.")
    exit(1)

# Step 2: Data Augmentation and Preprocessing
augment_kwargs = dict(
    rescale=1.0 / 255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Detect explicit train/val split
train_dir = data_dir
val_dir = None
has_explicit_split = (
    os.path.isdir(os.path.join(data_dir, 'train'))
    and os.path.isdir(os.path.join(data_dir, 'val'))
    and _directory_has_images(os.path.join(data_dir, 'train'))
    and _directory_has_images(os.path.join(data_dir, 'val'))
)

if has_explicit_split:
    print("\nDetected 'train' and 'val' folders. Using them directly.")
    train_dir = os.path.join(data_dir, 'train')
    val_dir = os.path.join(data_dir, 'val')
    train_data_gen = ImageDataGenerator(**augment_kwargs)
    val_data_gen = ImageDataGenerator(rescale=1.0 / 255)
else:
    print("\nUsing single directory with validation_split=0.2.")
    train_data_gen = ImageDataGenerator(validation_split=0.2, **augment_kwargs)
    val_data_gen = ImageDataGenerator(rescale=1.0 / 255, validation_split=0.2)

print("\nLoading training data...")
train_data = train_data_gen.flow_from_directory(
    train_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='training' if not has_explicit_split else None
)

class_indices = train_data.class_indices
class_names = sorted(class_indices, key=lambda k: class_indices[k])
num_classes = len(class_names)
print(f"Detected classes ({num_classes}): {class_names}")

print("Loading validation data...")
if has_explicit_split:
    val_data = val_data_gen.flow_from_directory(
        val_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=False,
        classes=class_names
    )
else:
    val_data = val_data_gen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation',
        shuffle=False
    )

# Step 2.1: Compute Class Weights
print("\nComputing class weights...")
class_labels = train_data.classes
class_weights = compute_class_weight(
    class_weight='balanced',
    classes=np.unique(class_labels),
    y=class_labels
)
class_weights = dict(enumerate(class_weights))
print(f"Class weights: {class_weights}")

# Step 3: Build the Model
print("\nBuilding model...")
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(128, 128, 3),
    include_top=False,
    weights='imagenet'
)

# Fine-tune: unfreeze last 50 layers
base_model.trainable = True
for layer in base_model.layers[:-50]:
    layer.trainable = False

model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    Dropout(0.6),
    Dense(num_classes, activation='softmax')
])

# Step 4: Compile Model
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.0001,
    decay_steps=10000,
    decay_rate=0.9
)

optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule)

model.compile(
    optimizer=optimizer,
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("Model compiled successfully!")
print(f"Total parameters: {model.count_params():,}")

# Step 5: Training
print("\nStarting training...")
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

history = model.fit(
    train_data,
    epochs=100,
    validation_data=val_data,
    callbacks=[early_stopping],
    class_weight=class_weights
)

# Step 6: Save Model
print(f"\nSaving model to: {MODEL_SAVE_PATH}")
model.save(MODEL_SAVE_PATH)
print("Model saved successfully!")

print(f"Saving class names to: {CLASS_NAMES_PATH}")
with open(CLASS_NAMES_PATH, 'w', encoding='utf-8') as f:
    json.dump(class_names, f, indent=4)

# Final metrics
print("\nTraining completed!")
print(f"Final training accuracy: {history.history['accuracy'][-1]:.4f}")
print(f"Final validation accuracy: {history.history['val_accuracy'][-1]:.4f}")
print(f"\nModel is ready to use at: {MODEL_SAVE_PATH}")
