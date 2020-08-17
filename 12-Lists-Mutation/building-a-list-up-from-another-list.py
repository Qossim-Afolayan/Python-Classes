powerball_numbers = [4, 8, 15, 23, 42]

def squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)

    return squares

print(squares(powerball_numbers))

def convert_to_float(numbers):
    floats = []
    for number in numbers:
        floats.append(float(number))

    return floats

print(convert_to_float(powerball_numbers))

# def even_or_odd(numbers):
#     booleans = []
#     for number in numbers:
#         result = 0
#         if number % 2 == 0:
#             result = True

#         else:
#             result = False

#         booleans.append(result)

#     return booleans

# print(even_or_odd(powerball_numbers))

def even_or_odd(numbers):
    booleans = []
    for number in numbers:
        if number % 2 == 0:
            booleans.append(True)
        else:
            booleans.append(False)
    return booleans

print(even_or_odd(powerball_numbers))

