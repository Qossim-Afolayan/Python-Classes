nintendo_games = ["Zelda", "Mario", "Donkey Kong", "Zelda"]

nintendo_games.remove("Zelda")
print(nintendo_games)

nintendo_games.remove("Zelda")
print(nintendo_games)

def delete_all(strings, target):
    result = []
    for number in strings:
        if number == target:
            continue
        else:
            result.append(number)
            
    return result

print(delete_all([1, 3, 5], 3))
print(delete_all([4, 4, 4], 6))

# def delete_all(strings, target):
#     if target in strings:
#         strings.remove(target)

#     return strings

# print(delete_all([1, 3, 5], 3))
# print(delete_all([4, 4, 4], 6))
# print(delete_all([4, 4, 4], 4))
def push_or_pop(numbers):
    total = []
    for number in numbers:
        if number > 5:
            total.append(number)
        else:
            total.pop()
    return total

print(push_or_pop([10, 20, 30]))
print(push_or_pop([10, 20, 2, 30]))






