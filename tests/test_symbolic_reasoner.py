import unittest
from symbolicai.symbolic_reasoner import SymbolicReasoner

class TestSymbolicReasoner(unittest.TestCase):
    def test_add_query_remove(self):
        sr = SymbolicReasoner()
        sr.add_fact("a", 1)
        self.assertEqual(sr.query("a"), 1)
        sr.remove_fact("a")
        self.assertIsNone(sr.query("a"))

    def test_apply_rule(self):
        sr = SymbolicReasoner()
        sr.add_fact("x", 2)
        def rule(kb):
            return kb["x"] * 2
        self.assertEqual(sr.apply_rule(rule), 4)

    def test_chain_rules(self):
        sr = SymbolicReasoner()
        sr.add_fact("x", 2)
        def rule1(kb): return kb["x"] + 1
        def rule2(kb): return kb["x"] * 3
        results = sr.chain_rules([rule1, rule2])
        self.assertEqual(results, [3, 6])

    def test_contradiction(self):
        sr = SymbolicReasoner()
        sr.add_fact("y", 5)
        sr.add_fact("y", 10)
        self.assertTrue(len(sr.contradictions) > 0)

if __name__ == "__main__":
    unittest.main()
