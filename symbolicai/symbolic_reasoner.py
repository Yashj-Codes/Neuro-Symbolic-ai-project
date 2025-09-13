import json

class SymbolicReasoner:
    """
    Neuro-symbolic reasoner with knowledge base, inference, contradiction handling, and pretty-printing.
    """
    def __init__(self):
        self.knowledge_base = {}
        self.reasoning_steps = []
        self.contradictions = []

    def add_fact(self, key, value):
        if key in self.knowledge_base and self.knowledge_base[key] != value:
            self.contradictions.append((key, self.knowledge_base[key], value))
            self.reasoning_steps.append(f"Contradiction: {key} was {self.knowledge_base[key]}, now {value}")
        self.knowledge_base[key] = value
        self.reasoning_steps.append(f"Added fact: {key} = {value}")

    def update_fact(self, key, value):
        self.add_fact(key, value)

    def remove_fact(self, key):
        if key in self.knowledge_base:
            del self.knowledge_base[key]
            self.reasoning_steps.append(f"Removed fact: {key}")

    def query(self, key):
        return self.knowledge_base.get(key, None)

    def apply_rule(self, rule_func):
        result = rule_func(self.knowledge_base)
        self.reasoning_steps.append(f"Applied rule: {rule_func.__name__} → {result}")
        return result

    def chain_rules(self, rules):
        results = []
        for rule in rules:
            results.append(self.apply_rule(rule))
        return results

    def pretty_print(self):
        print("=== Reasoning Steps ===")
        for step in self.reasoning_steps:
            print(step)
        if self.contradictions:
            print("--- Contradictions ---")
            for c in self.contradictions:
                print(f"Key: {c[0]}, Old: {c[1]}, New: {c[2]}")
        print("--- Knowledge Base ---")
        for k, v in self.knowledge_base.items():
            print(f"{k}: {v}")
        print("======================")

    def save(self, path):
        with open(path, "w") as f:
            json.dump(self.knowledge_base, f)

    def load(self, path):
        with open(path, "r") as f:
            self.knowledge_base = json.load(f)
