import streamlit as st
from symbolicai.symbolic_reasoner import SymbolicReasoner
from symbolicai.neural_module import NeuralModule
from symbolicai.symbolic_mapper import SymbolicMapper
from symbolicai.rule_engine import RuleEngine
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

def print_output(output, facts):
    st.markdown("### Neuro-Symbolic Legal Reasoner Output")
    st.write(f"**Conclusion:** {output['Conclusion']}")
    st.write("**Reasoning Explanation:**")
    for idx, step in enumerate(output["Reasoning Explanation"], 1):
        st.write(f"{idx}. {step}")
    st.write("**Facts Extracted:**")
    for key, value in facts.items():
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
        extracted_facts = extract_facts_from_clause(clause)
        mapper = SymbolicMapper()
        symbolic_facts = mapper.map_facts(extracted_facts)
        rule_engine = RuleEngine(symbolic_facts)
        output = rule_engine.apply_rules()
        print_output(output, symbolic_facts)

if __name__ == "__main__":
    main()
