def add(x, y):
    assert isinstance(x, int) and isinstance(y, int)
    return x + y

print(add(3, 5))
# print(add(3, "5")) #AssertionError

