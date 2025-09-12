class SymbolicReasoner:
    """
    A simple symbolic reasoner for neuro-symbolic AI.
    """
    def __init__(self):
        self.knowledge_base = {}

    def add_fact(self, key, value):
        self.knowledge_base[key] = value

    def query(self, key):
        return self.knowledge_base.get(key, None)

    def infer(self, rule_func):
        """
        Apply a rule function to the knowledge base for inference.
        """
        return rule_func(self.knowledge_base)
