from symbolicai.neural_module import NeuralModule
from symbolicai.symbolic_reasoner import SymbolicReasoner

class HybridEngine:
    """
    Combines NeuralModule and SymbolicReasoner for neuro-symbolic inference.
    """
    def __init__(self, input_dim, output_dim):
        self.neural = NeuralModule(input_dim, output_dim)
        self.symbolic = SymbolicReasoner()

    def process(self, x):
        neural_pred = self.neural.forward(x)
        # Example: convert neural prediction to symbolic fact
        fact = "input is large" if neural_pred.mean() > 0.5 else "input is small"
        self.symbolic.add_fact("input_size", fact)
        # Symbolic rule: If "input is large", explanation = "High Risk"
        def risk_rule(kb):
            return "High Risk" if kb.get("input_size") == "input is large" else "Low Risk"
        explanation = self.symbolic.apply_rule(risk_rule)
        return {
            "neural_prediction": neural_pred,
            "symbolic_explanation": explanation,
            "reasoning_steps": self.symbolic.reasoning_steps
        }
