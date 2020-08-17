def height_to_meters(feet, inches):
    total_inches = feet * 12 + inches
    return total_inches * 0.0254

print(height_to_meters(5, 11))

stats = {
    "feet": 5,
    "inches": 11
}

print(height_to_meters(**stats))

# def plenty_of_arguments(a, b, **kwargs):
#     if sum(tuple(kwargs.values())) + a + b > 100:
#         return True
#     else:
#         return False
def plenty_of_arguments(a, b, **kwargs):
    return sum(kwargs.values()) + a + b > 100
print(plenty_of_arguments(a = 50, b = 25, c = 50))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 25))
print(plenty_of_arguments(a = 50, b = 75))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26))

