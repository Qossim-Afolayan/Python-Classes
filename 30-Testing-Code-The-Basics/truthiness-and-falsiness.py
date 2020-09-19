import unittest

class TestTruthinessAndFalsiness(unittest.TestCase):
    def test_truthiness(self):
        #self.assertEqual(3 < 5, True)
        self.assertTrue(3 < 5)
        self.assertTrue("hello")
        # self.assertTrue(0)
        self.assertTrue("a")
        self.assertTrue({"b": 2})

    def test_falsiness(self):
        self.assertFalse(0)
        self.assertFalse("")
        self.assertFalse([])
        self.assertFalse({})
        self.assertFalse(False)

if __name__ == "__main__":
    unittest.main()

    