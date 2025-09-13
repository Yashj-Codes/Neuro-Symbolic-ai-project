class RuleEngine:
    """
    Applies logical rules to symbolic facts for contract reasoning.
    """
    def __init__(self, facts):
        self.facts = facts
        self.rules_applied = []
        self.explanation = []

    def apply_rules(self):
        # Example rule logic
        if self.facts.get("Payment Date", "") > self.facts.get("Due Date", ""):
            self.rules_applied.append("Exception triggered: delayed payment by Buyer")
            self.explanation.append("Exception in clause: Seller not liable for late delivery if Buyer delays payment.")
            if self.facts.get("Delivery Date", "") > self.facts.get("Due Date", ""):
                conclusion = "Seller is NOT in breach of contract."
                self.rules_applied.append("Breach check: No breach detected")
                self.explanation.append("Seller delivered laptops after payment, so late delivery is excused.")
            else:
                conclusion = "Seller delivered on time."
                self.rules_applied.append("Breach check: No breach detected")
                self.explanation.append("Seller delivered on time despite late payment.")
        else:
            if self.facts.get("Delivery Date", "") > self.facts.get("Due Date", ""):
                conclusion = "Seller IS in breach of contract."
                self.rules_applied.append("Breach check: Breach detected")
                self.explanation.append("Seller delivered late without excusable reason.")
            else:
                conclusion = "Seller delivered on time."
                self.rules_applied.append("Breach check: No breach detected")
                self.explanation.append("Seller delivered on time.")
        return {
            "Conclusion": conclusion,
            "Reasoning Explanation": self.explanation,
            "Applied Rules": self.rules_applied
        }
