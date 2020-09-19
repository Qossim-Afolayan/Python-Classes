import unittest

class TestObjectIdentity(unittest.TestCase):
    def test_identiy(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertEqual(a, b)
        self.assertEqual(a, c)

        self.assertIs(a, b)
        # self.assertIs(a, c)
        # self.assertIs(b, c)

if __name__ == "__main__":
    unittest.main()