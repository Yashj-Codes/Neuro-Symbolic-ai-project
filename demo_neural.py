import numpy as np
from symbolicai.neural_module import NeuralModule

input_dim = 3
output_dim = 2
neural = NeuralModule(input_dim, output_dim)

# Generate toy data
X = np.random.rand(100, input_dim)
y = np.random.rand(100, output_dim)

print("Predictions before training:")
preds_before = neural.forward(X)
print(preds_before[:5])

neural.train(X, y, lr=0.01, epochs=50)

print("Predictions after training:")
preds_after = neural.forward(X)
print(preds_after[:5])

neural.print_weights()
