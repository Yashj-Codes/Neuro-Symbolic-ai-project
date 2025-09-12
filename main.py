import streamlit as st
from symbolicai.symbolic_reasoner import SymbolicReasoner
from symbolicai.neural_module import NeuralModule
import numpy as np

# Neural module for extracting facts (placeholder)
def extract_facts_from_clause(clause):
    # Placeholder extraction logic
    return {
        "Parties": ["Seller", "Buyer"],
        "Obligation": "deliver 100 laptops",
        "Due Date": "2025-10-01",
        "Condition": "Payment by Buyer before due date",
        "Exception": "Seller not liable for late delivery if Buyer delays payment",
        "Payment Date": "2025-10-05",
        "Delivery Date": "2025-10-07"
    }

# Symbolic reasoning function
def infer_breach(facts):
    reasoner = SymbolicReasoner()
    for k, v in facts.items():
        reasoner.add_fact(k, v)
    rules = []
    explanation = []
    # Reasoning logic
    if facts["Payment Date"] > facts["Due Date"]:
        rules.append("Exception triggered: delayed payment by Buyer")
        explanation.append("Exception in clause: Seller not liable for late delivery if Buyer delays payment.")
        if facts["Delivery Date"] > facts["Due Date"]:
            conclusion = "Seller is NOT in breach of contract."
            rules.append("Breach check: No breach detected")
            explanation.append("Seller delivered laptops after payment, so late delivery is excused.")
        else:
            conclusion = "Seller delivered on time."
            rules.append("Breach check: No breach detected")
            explanation.append("Seller delivered on time despite late payment.")
    else:
        if facts["Delivery Date"] > facts["Due Date"]:
            conclusion = "Seller IS in breach of contract."
            rules.append("Breach check: Breach detected")
            explanation.append("Seller delivered late without excusable reason.")
        else:
            conclusion = "Seller delivered on time."
            rules.append("Breach check: No breach detected")
            explanation.append("Seller delivered on time.")
    return {
        "Conclusion": conclusion,
        "Reasoning Explanation": explanation,
        "Facts Extracted": facts,
        "Applied Rules": rules
    }

def print_output(output):
    st.markdown("### Neuro-Symbolic Legal Reasoner Output")
    st.write(f"**Conclusion:** {output['Conclusion']}")
    st.write("**Reasoning Explanation:**")
    for idx, step in enumerate(output["Reasoning Explanation"], 1):
        st.write(f"{idx}. {step}")
    st.write("**Facts Extracted:**")
    for key, value in output["Facts Extracted"].items():
        st.write(f"- {key}: {value}")
    st.write("**Applied Rules:**")
    for rule in output["Applied Rules"]:
        st.write(f"- {rule}")
    st.write("---")

# Streamlit UI
def main():
    st.title("Neuro-Symbolic Legal Reasoning Demo")
    clause = st.text_area("Enter contract clause:", "Seller must deliver 100 laptops by Oct 1, 2025, provided Buyer pays before due date. If Buyer pays late, Seller is not liable for late delivery.")
    if st.button("Analyze Clause"):
        facts = extract_facts_from_clause(clause)
        output = infer_breach(facts)
        print_output(output)

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

if __name__ == "__main__":
    main()
