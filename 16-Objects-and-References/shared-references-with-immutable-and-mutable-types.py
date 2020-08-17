#imutable object; numbers, booleans, strings and tuples
a = 3
b = a

a = 5
print(a)
print(b)

#mutable object
a = [1, 2, 3]
b = a

a.append(4)
print(a)
print(b)

a.append(5)
print(a)
print(b)


