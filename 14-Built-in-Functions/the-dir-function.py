# users = "Bob, Dave, John, Sun, Randy, Meg"

# print(users.split(", "))

# print(users.split(", ", 3))

# print(dir([])) #dunder methods (secret)

print(dir("pasta"))

print(len("pasta"))

print("pasta".__len__()) #behind the scenes

print("st" in "pasta")
print("pasta".__contains__("st"))

print('pasta' + " and meatballs")
print("pasta".__add__(" and meatballs"))