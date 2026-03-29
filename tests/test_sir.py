# tests/test_sir.py
import sys
sys.path.append('../src')
import pytest
import torch
from sir_model import load_sir_model, predict_depth

def test_model_load():
    model = load_sir_model()
    assert model is not None

def test_predict_shape():
    model = load_sir_model()
    dummy_img = torch.rand(1, 3, 224, 224)
    depth = predict_depth(model, dummy_img)
    assert depth.shape == (1, 1, 224, 224)  # Adjust to your model

# Run: pytest tests/