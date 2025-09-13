import unittest
import numpy as np
from symbolicai.hybrid_engine import HybridEngine

class TestHybridEngine(unittest.TestCase):
    def test_hybrid_integration(self):
        he = HybridEngine(3, 1)
        x = np.array([1.0, 2.0, 3.0])
        result = he.process(x)
        self.assertIn("neural_prediction", result)
        self.assertIn("symbolic_explanation", result)
        self.assertIn("reasoning_steps", result)

    def test_multiple_rules(self):
        he = HybridEngine(3, 1)
        x = np.array([10.0, 10.0, 10.0])
        result = he.process(x)
        self.assertEqual(result["symbolic_explanation"], "High Risk")
        x = np.array([0.1, 0.1, 0.1])
        result = he.process(x)
        self.assertEqual(result["symbolic_explanation"], "Low Risk")

if __name__ == "__main__":
    unittest.main()
