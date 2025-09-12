# Neuro-Symbolic AI Project

This project demonstrates a simple neuro-symbolic AI system, combining symbolic reasoning with neural network modules. Inspired by the ExtensityAI/symbolicai repository, this implementation is original and provides a foundation for further research and experimentation.

## Features
- Symbolic reasoner for knowledge representation and inference
- Neural module for basic vector transformations
- Example usage integrating both symbolic and neural components

## Getting Started
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install numpy
   ```
3. Run the main script:
   ```bash
   python main.py
   ```

## Example Output
```
=== Neuro-Symbolic Legal Reasoner Output ===

Conclusion: Seller is NOT in breach of contract.

Reasoning Explanation:
1. Clause requires Seller to deliver 100 laptops by Oct 1, 2025, if Buyer pays on time.
2. Buyer paid late (Oct 5, 2025).
3. Exception in clause: Seller not liable for late delivery if Buyer delays payment.
4. Seller delivered laptops on Oct 7, 2025.
5. Therefore, the Seller’s late delivery does not constitute a breach.

Facts Extracted:
- Parties: ['Seller', 'Buyer']
- Obligation: deliver 100 laptops
- Due Date: 2025-10-01
- Condition: Payment by Buyer before due date
- Payment Date: 2025-10-05
- Delivery Date: 2025-10-07

Applied Rules:
- Exception triggered: delayed payment by Buyer
- Breach check: No breach detected

----------------------------------------
```

## Project Structure
- `symbolicai/`: Core package
  - `symbolic_reasoner.py`: Symbolic reasoning engine
  - `neural_module.py`: Simple neural module
- `main.py`: Example usage

## License
This project is open source and free to use for educational and research purposes.
