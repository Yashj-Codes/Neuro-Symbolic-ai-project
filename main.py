from symbolicai.symbolic_reasoner import SymbolicReasoner
from symbolicai.neural_module import NeuralModule
import numpy as np

def main():
    # Symbolic Reasoning Example
    reasoner = SymbolicReasoner()
    reasoner.add_fact('sky', 'blue')
    reasoner.add_fact('grass', 'green')
    print('Query sky:', reasoner.query('sky'))
    print('Query grass:', reasoner.query('grass'))

    def rule(kb):
        return 'The world is colorful' if 'sky' in kb and 'grass' in kb else 'Incomplete knowledge'
    print('Inference:', reasoner.infer(rule))

    # Neural Module Example
    neural = NeuralModule(input_dim=3, output_dim=2)
    x = np.array([1.0, 2.0, 3.0])
    print('Neural output:', neural.forward(x))

if __name__ == '__main__':
    main()
