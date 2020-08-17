animals = ["elephant", 'giraffe', "cat", "horse"]
print([animal for animal in animals if len(animal) > 5])

def is_long_animal(animal):
    return len(animal) > 5

print(list(filter(is_long_animal, animals)))

#the function should return a boolean
values = [3.45, 5.67, 7.89]

square_map = list(map(lambda x: x * x, values))
print(square_map)
