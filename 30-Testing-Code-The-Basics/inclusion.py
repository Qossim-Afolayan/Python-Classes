import unittest

class InclusionTests(unittest.TestCase):
    def test_inclusion(self):
        #self.asssertTrue("k" in "king")

        self.assertIn("k", "king")
        self.assertIn(1, [1, 2, 3, 4])
        self.assertIn(5, (5, 6, 7))
        self.assertIn("a",{"a": 1, "b": 2}.keys())
        self.assertIn(1,{"a": 1, "b": 2}.values())
        self.assertIn(44, range(42, 45))

    def test_non_inclusion(self):
        self.assertNotIn("w", "king")
        self.assertNotIn(6, [1, 2, 3, 4])
        self.assertNotIn(8, (5, 6, 7))
        self.assertNotIn("f",{"a": 1, "b": 2}.keys())
        self.assertNotIn(5, {"a": 1, "b": 2}.values())
        self.assertNotIn(55, range(42, 45))

if __name__ == "__main__":
    unittest.main()

    
