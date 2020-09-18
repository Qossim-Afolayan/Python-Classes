def add(x, y):
    assert isinstance(x, int) and isinstance(y, int)
    return x + y

print(add(3, 5))
# print(add(3, "5")) #AssertionError
import unittest
class TestStringMethods(unittest.TestCase):

    def test_split(self):

      self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])



    def test_count(self):

      self.assertEqual("beautiful".count("u"), 2)



    def test_swapcase(self):
        self.assertEqual("qossim".swapcase(), "QOSSIM")



    def test_index(self):
        self.assertEqual("qossim".index("q"), 0)



if __name__ == "__main__":

  unittest.main()