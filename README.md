# Neuro-Symbolic AI Project

This project demonstrates a simple neuro-symbolic AI system, combining symbolic reasoning with neural network modules. Inspired by the ExtensityAI/symbolicai repository, this implementation is original and provides a foundation for further research and experimentation.

# 🚀 Project Overview

The Neuro-Symbolic Legal Reasoning System is a hybrid AI application that combines neural networks and symbolic reasoning to analyze legal documents, such as contracts, and generate explainable conclusions.

Neural Extraction: Uses NLP models (e.g., Legal-BERT) to extract parties, obligations, dates, conditions, and exceptions from contract clauses.

Symbolic Reasoning: Applies predefined rules using symbolic logic (Prolog or SymbolicAI) to determine breaches, liability, and rights.

Explainability: Produces a reasoning chain that shows exactly why a decision was made.

Demo Ready: Can be extended with a simple web interface using Streamlit or Flask for interactive use.

This project showcases the integration of modern deep learning with traditional symbolic AI, making decisions interpretable and auditable.

💡 Key Features

- Contract Clause Analysis
  - Extracts entities like parties, obligations, payment terms, and exceptions.
  - Converts extracted data into structured symbolic facts.
- Rule-Based Reasoning
  - Implements logical rules for breach detection.
  - Handles exceptions, conditions, and temporal constraints.
- Explainable Output
  - Generates human-readable explanations showing the reasoning steps.
  - Outputs structured facts, applied rules, and final conclusions.
- Extensible Architecture
  - Easy to add new domain-specific rules.
  - Can integrate with neural models for other domains (e.g., traffic laws).

🏗️ Project Architecture
```
   +-----------------+
   |  Input Clause   |
   |  (Contract)     |
   +--------+--------+
            |
            v
   +-----------------+
   | Neural Extractor|
   | (Legal-BERT,   |
   |  spaCy NER)     |
   +--------+--------+
            |
            v
   +-----------------+
   | Symbolic Mapper |
   | (Prolog/KB)     |
   +--------+--------+
            |
            v
   +-----------------+
   | Rule Engine     |
   | (Logic/Contracts|
   |  SymbolicAI)    |
   +--------+--------+
            |
            v
   +-----------------+
   | Explanation Gen |
   | (Reasoning Chain|
   +-----------------+
```

🛠️ Technologies Used

- Symbolic Reasoning: Prolog / SymbolicAI
- Neural NLP Models: Legal-BERT, spaCy
- Programming Language: Python 3.11+
- Web Interface (optional): Streamlit / Flask
- Version Control: Git + GitHub
- Visualization: Reasoning chains printed or displayed in UI

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
