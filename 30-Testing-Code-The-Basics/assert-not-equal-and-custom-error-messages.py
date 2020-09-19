import unittest

def copy_and_add_element(values, element):
    copy = values[:]
    copy.append(element)
    return copy

class TestNotEqual(unittest.TestCase):
    def test_inequality(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual(True, False)
        self.assertNotEqual("Hello", "hello")
        self.assertNotEqual([1, 2], [2, 3])

    def test_copy_and_add_element(self):
        values = [1, 2, 3]
        result = copy_and_add_element(values, 4)

        self.assertEqual(result, [1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()