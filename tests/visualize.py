# scripts/visualize.py - Plotly depth viz
import torch
import plotly.graph_objects as go
import numpy as np
from sir_model import predict_depth
import sys
sys.path.append('../src')

def viz_depth(model, image):
    depth = predict_depth(model, image)[0,0].cpu().numpy()
    fig = go.Figure(data=go.Heatmap(z=depth))
    fig.update_layout(title="SIR Depth Map")
    fig.write_html("output/depth_viz.html")
    fig.show()

if __name__ == "__main__":
    model = load_sir_model()
    # dummy_img = torch.rand(1,3,224,224)
    # viz_depth(model, dummy_img)
    print("Run: python scripts/visualize.py")