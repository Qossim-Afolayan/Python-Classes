import unittest

def explicit_return_sum(a, b):
    return a + b

def implicit_return_sum(a, b):
    print(a + b)

class TestNullness(unittest.TestCase):
    def test_sum_function(self):
        self.assertIsNone(implicit_return_sum(4, 4))
        self.assertIsNotNone(explicit_return_sum(3, 4))

if __name__ == "__main__":
    unittest.main()