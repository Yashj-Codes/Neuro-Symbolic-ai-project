class RuleEngine:
    """
    Applies logical rules to symbolic facts for contract reasoning.
    """
    def __init__(self, facts):
        self.facts = facts
        self.rules_applied = []
        self.explanation = []

    def apply_rules(self):
        # Safely compare dates, handle None values
        payment_date = self.facts.get("Payment Date")
        due_date = self.facts.get("Due Date")
        delivery_date = self.facts.get("Delivery Date")
        conclusion = "No conclusion"
        self.rules_applied = []
        self.explanation = []
        # Only compare if both dates are valid strings
        if payment_date and due_date and payment_date != "Unknown" and due_date != "Unknown":
            if payment_date > due_date:
                self.rules_applied.append("Exception triggered: delayed payment by Buyer")
                self.explanation.append("Exception in clause: Seller not liable for late delivery if Buyer delays payment.")
                if delivery_date and delivery_date != "Unknown" and delivery_date > due_date:
                    conclusion = "Seller is NOT in breach of contract."
                    self.rules_applied.append("Breach check: No breach detected")
                    self.explanation.append("Seller delivered laptops after payment, so late delivery is excused.")
                else:
                    conclusion = "Seller delivered on time."
                    self.rules_applied.append("Breach check: No breach detected")
                    self.explanation.append("Seller delivered on time despite late payment.")
            else:
                if delivery_date and delivery_date != "Unknown" and delivery_date > due_date:
                    conclusion = "Seller IS in breach of contract."
                    self.rules_applied.append("Breach check: Breach detected")
                    self.explanation.append("Seller delivered late without excusable reason.")
                else:
                    conclusion = "Seller delivered on time."
                    self.rules_applied.append("Breach check: No breach detected")
                    self.explanation.append("Seller delivered on time.")
        else:
            conclusion = "Insufficient date information for reasoning."
            self.rules_applied.append("No breach check performed")
            self.explanation.append("Missing or unknown payment/due/delivery date.")
        return {
            "Conclusion": conclusion,
            "Reasoning Explanation": self.explanation,
            "Applied Rules": self.rules_applied
        }
