#Variables only point to objets and not variables
a = b = 5

a = 10
print(a)
print(b)

a, b = 10, 11
print(a, b)
