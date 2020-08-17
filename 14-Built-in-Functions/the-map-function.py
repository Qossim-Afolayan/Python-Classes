numbers = [15, 20, 35, 29]
print([number ** 2 for number in numbers])

def cube(number):
    return number ** 3

print(list(map(cube, numbers)))

animals = ["cat", "donkey", "zebra", "cheetah"]
print([len(animal) for animal in animals])
print(list(map(len, animals)))