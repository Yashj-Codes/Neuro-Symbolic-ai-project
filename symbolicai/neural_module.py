import numpy as np
import pickle

class NeuralModule:
    """
    Simple neural module for neuro-symbolic AI with linear model, activation, training, and persistence.
    """
    def __init__(self, input_dim, output_dim, activation="relu"):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.weights = np.random.randn(input_dim, output_dim)
        self.activation = activation

    def forward(self, x):
        z = np.dot(x, self.weights)
        if self.activation == "relu":
            return np.maximum(0, z)
        elif self.activation == "sigmoid":
            return 1 / (1 + np.exp(-z))
        else:
            return z

    def train(self, X, y, lr=0.01, epochs=100):
        for epoch in range(epochs):
            preds = self.forward(X)
            loss = np.mean((preds - y) ** 2)
            grad = 2 * np.dot(X.T, (preds - y)) / X.shape[0]
            self.weights -= lr * grad
            if epoch % 10 == 0:
                print(f"Epoch {epoch}: Loss = {loss:.4f}")
        print(f"Training complete. Final loss: {loss:.4f}")

    def save(self, path):
        with open(path, "wb") as f:
            pickle.dump(self.weights, f)
        print(f"Weights saved to {path}")

    def load(self, path):
        with open(path, "rb") as f:
            self.weights = pickle.load(f)
        print(f"Weights loaded from {path}")

    def print_weights(self):
        print(f"Weights shape: {self.weights.shape}")
        print(self.weights)
