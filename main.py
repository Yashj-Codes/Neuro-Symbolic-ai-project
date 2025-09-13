import streamlit as st
from symbolicai.symbolic_reasoner import SymbolicReasoner
from symbolicai.neural_module import NeuralModule
from symbolicai.symbolic_mapper import SymbolicMapper
from symbolicai.rule_engine import RuleEngine
import numpy as np
import spacy
import dateparser

nlp = spacy.load("en_core_web_sm")

# Advanced NLP-based fact extraction
def extract_facts_from_clause(clause):
    doc = nlp(clause)
    parties = [ent.text for ent in doc.ents if ent.label_ in ["PERSON", "ORG"]]
    dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
    money = [ent.text for ent in doc.ents if ent.label_ == "MONEY"]
    obligation = None
    exception = None
    condition = None
    # Simple heuristics for obligations, exceptions, conditions
    if "deliver" in clause:
        obligation = "deliver " + next((token.text for token in doc if token.text.isdigit()), "items")
    elif "pay" in clause:
        obligation = "pay " + (money[0] if money else "amount")
    elif "complete installation" in clause:
        obligation = "complete installation"
    elif "vacate" in clause:
        obligation = "vacate premises"
    elif "finish project" in clause:
        obligation = "finish project"
    # Exception and condition extraction
    if "unless" in clause:
        exception = clause.split("unless")[-1].strip()
    if "if" in clause:
        condition = clause.split("if")[-1].strip()
    # Date parsing
    if dates:
        parsed_due = dateparser.parse(dates[0])
        due_date = parsed_due.strftime("%Y-%m-%d") if parsed_due else "Unknown"
    else:
        due_date = "Unknown"
    payment_date = None
    delivery_date = None
    # Return structured facts
    return {
        "Parties": parties if parties else ["Unknown"],
        "Obligation": obligation if obligation else "Unknown",
        "Due Date": due_date if due_date else "Unknown",
        "Condition": condition,
        "Exception": exception,
        "Payment Date": payment_date,
        "Delivery Date": delivery_date
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
    # Additional details
    st.write("**Full Clause:**")
    st.code(st.session_state.get('clause_text', ''), language='text')
    st.write("**Entities Detected:**")
    st.json({
        "Parties": facts.get("Parties", []),
        "Dates": facts.get("Due Date", "Unknown"),
        "Obligation": facts.get("Obligation", "Unknown"),
        "Condition": facts.get("Condition", None),
        "Exception": facts.get("Exception", None),
        "Payment Date": facts.get("Payment Date", None),
        "Delivery Date": facts.get("Delivery Date", None)
    })
    st.write("**Symbolic Reasoner Knowledge Base:**")
    st.json(facts)

# Streamlit UI
def main():
    st.title("Neuro-Symbolic Legal Reasoning Demo")
    example_clauses = [
        "Seller must deliver 100 laptops by Oct 1, 2025, provided Buyer pays before due date. If Buyer pays late, Seller is not liable for late delivery.",
        "Buyer must pay $10,000 by Nov 15, 2025. If payment is late, interest of 5% applies.",
        "Service provider must complete installation by Dec 31, 2025, unless delayed by force majeure.",
        "Tenant must vacate premises by Jan 1, 2026, unless lease is renewed.",
        "Contractor must finish project by Mar 1, 2026. If weather delays, deadline extends by 7 days."
    ]
    clause = st.selectbox("Choose an example contract clause or enter your own:", example_clauses)
    custom_clause = st.text_area("Or enter a custom clause:", "")
    final_clause = custom_clause if custom_clause.strip() else clause
    st.session_state['clause_text'] = final_clause
    if st.button("Analyze Clause"):
        extracted_facts = extract_facts_from_clause(final_clause)
        mapper = SymbolicMapper()
        symbolic_facts = mapper.map_facts(extracted_facts)
        rule_engine = RuleEngine(symbolic_facts)
        output = rule_engine.apply_rules()
        print_output(output, symbolic_facts)

if __name__ == "__main__":
    main()
