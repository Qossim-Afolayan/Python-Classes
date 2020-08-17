#Default Argument: Fallback arguments that are passed to a function if an explicit value is not provided for a parameter
def add(a = 3, b = 4, c = 5):
    return a + b + c

print(add(3, 6, 7))
print(add())