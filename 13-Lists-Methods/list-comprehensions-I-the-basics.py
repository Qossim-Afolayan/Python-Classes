numbers = [2, 4, 6, 8, 10]
squares = []
for number in numbers:
    squares.append(number ** 2)

print(squares)

print([number ** 2 for number in numbers])

rivers = ["Amazon", "Nile", "Yutze"]
print([len(river) for river in rivers])

expressions = ["lol", 'rofl']
print([expression.upper() for expression in expressions])

decimals = [2.45, 3.70, 4.56, 9.08]
print([int(decimal) for decimal in decimals])




