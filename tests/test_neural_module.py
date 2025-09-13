import unittest
import numpy as np
from symbolicai.neural_module import NeuralModule
import os

class TestNeuralModule(unittest.TestCase):
    def test_forward_shape(self):
        nm = NeuralModule(3, 2)
        x = np.random.rand(5, 3)
        out = nm.forward(x)
        self.assertEqual(out.shape, (5, 2))

    def test_training_reduces_loss(self):
        nm = NeuralModule(3, 1)
        X = np.random.rand(50, 3)
        y = np.random.rand(50, 1)
        preds_before = nm.forward(X)
        loss_before = np.mean((preds_before - y) ** 2)
        nm.train(X, y, lr=0.01, epochs=30)
        preds_after = nm.forward(X)
        loss_after = np.mean((preds_after - y) ** 2)
        self.assertLess(loss_after, loss_before)

    def test_save_load_weights(self):
        nm = NeuralModule(3, 2)
        path = "test_weights.pkl"
        nm.save(path)
        nm.weights += 1  # change weights
        nm.load(path)
        self.assertTrue(np.allclose(nm.weights, np.load(path, allow_pickle=True)))
        os.remove(path)

if __name__ == "__main__":
    unittest.main()
