#Assignment statements in Python do not copy objects, they create bindings 
# between a target and an object. For collections that are mutable or contain 
# mutable items, a copy is sometimes needed so one can change one copy without 
# changing the other.

# copy.copy(x)
# Return a shallow copy of x.

# copy.deepcopy(x[, memo])
# Return a deep copy of x.

#Shallow copy : one tier

#Deep copy : goes as deep as you wanna go

import copy

a = [1, 2, 3]

# b = a[:]
# print(a == b)
# print(a is b)

# c = a.copy()
# print(a == c)
# print(a is c)

# d = copy.copy(a)
# print(a == d)
# print(a is d)
numbers = [2, 3, 4]
a = [1, numbers, 5]
b = a[:]
b = a.copy()
b = copy.copy(a)
b = copy.deepcopy(a)
print(a == b)
print(a is b)
print(a[1] == b[1])
print(a[1] is b[1])

a[1].append(100)
print(b)

b[1].append(200)
print(a)
print(b)


