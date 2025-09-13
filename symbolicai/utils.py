import json
import numpy as np

# Pretty-print knowledge base
def print_kb(kb):
    print("--- Knowledge Base ---")
    for k, v in kb.items():
        print(f"{k}: {v}")
    print("----------------------")

# Simple dataset generator
def generate_dataset(n_samples=100, input_dim=3):
    X = np.random.rand(n_samples, input_dim)
    y = (X.sum(axis=1) > input_dim * 0.5).astype(float).reshape(-1, 1)
    return X, y

# Logging helper
def log(msg):
    print(f"[LOG] {msg}")

# Save/load knowledge base as JSON
def save_kb(kb, path):
    with open(path, "w") as f:
        json.dump(kb, f)

def load_kb(path):
    with open(path, "r") as f:
        return json.load(f)
