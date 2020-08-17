def product(a, b):
    return a * b


print(product(3, 5))

# numbers = [3, 5]
numbers = (3, 5)

print(product(*numbers))

qualities = ("Determination", "Grit", "Persverence", "Optimism", "Excitement")
*skills, traits = qualities

print(skills)