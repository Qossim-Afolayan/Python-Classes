import unittest

class ObjectTypeTests(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance(2.4, float)
        self.assertIsInstance([], list)
        self.assertIsInstance({"a": 1}, dict)

        # self.assertIsInstance({"a": 1}, list)
    def test_not_is_instance(self):
        self.assertNotIsInstance(1, float)
        self.assertNotIsInstance(2.3, int)
        self.assertNotIsInstance((), list)
        self.assertNotIsInstance([], tuple)
        self.assertNotIsInstance({}, list)

if __name__ == "__main__":
    unittest.main()

    