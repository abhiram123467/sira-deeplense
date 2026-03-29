import sys
sys.path.append('src')
from sir_model import load_sir_model, predict_depth



# src/sir_model.py - Extracted from SIRA_SIR_Model.ipynb
import torch
import torch.nn as nn
# Add your model imports/classes from notebook here

def load_sir_model(model_path='models/sir_model.pth'):
    """Load pretrained SIR model."""
    model = SIRModel()  # Replace with your model class
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def predict_depth(model, image):
    """Predict depth map from image."""
    with torch.no_grad():
        depth = model(image)
    return depth

if __name__ == "__main__":
    print("SIR model loaded!")