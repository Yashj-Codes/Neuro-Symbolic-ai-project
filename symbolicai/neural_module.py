import numpy as np

class NeuralModule:
    """
    A simple neural module for neuro-symbolic AI.
    """
    def __init__(self, input_dim, output_dim):
        self.weights = np.random.randn(input_dim, output_dim)

    def forward(self, x):
        return np.dot(x, self.weights)
