from symbolicai.symbolic_reasoner import SymbolicReasoner

def rule1(kb):
    return "sky is blue" if kb.get("sky") == "blue" else "sky is not blue"

def rule2(kb):
    return "grass is green" if kb.get("grass") == "green" else "grass is not green"

def contradiction_rule(kb):
    return "Contradiction detected" if "sky" in kb and kb["sky"] != "blue" else "No contradiction"

reasoner = SymbolicReasoner()
reasoner.add_fact("sky", "blue")
reasoner.add_fact("grass", "green")
reasoner.add_fact("sky", "red")  # Contradiction
print("Query sky:", reasoner.query("sky"))
print("Query grass:", reasoner.query("grass"))
results = reasoner.chain_rules([rule1, rule2, contradiction_rule])
print("Inference results:", results)
reasoner.pretty_print()
