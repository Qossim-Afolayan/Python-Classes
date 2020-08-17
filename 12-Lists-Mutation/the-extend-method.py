mountains = ["Mount Everest", "K2"]
print(mountains)

mountains.extend(["Kangchenjunga", "Lhotse", "Makalu"])
print(mountains)

extra_mountains = ["Cho Oyu", "Dhaulagiri"]
mountains.extend(extra_mountains)
print(mountains)

mountains.extend([])
print(mountains)

steaks = ["Tenderloin", "New York Strip"]
more_steaks = ["T-Bone", "Ribeye"]

my_meal = steaks + more_steaks
print(my_meal)
print(steaks)
print(more_steaks)

steaks += more_steaks
print(steaks)

def push_or_pop(numbers):
    total = []
    for index, number in enumerate(numbers):
        if number > 5:
            total.append(number)
        else:
            total.pop()
    return total

print(push_or_pop([10, 20, 30]))
print(push_or_pop([10, 20, 2, 30]))