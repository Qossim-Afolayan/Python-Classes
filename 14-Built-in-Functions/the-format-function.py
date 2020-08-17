#forrmat to modify a numeric value

number = 0.123456789
print(format(number, "f"))
print(type(format(number, "f")))


print(format(number, ".3f"))

print(format(0.5, "%"))
print(format(0.5, ".1%"))
print(format(0.5, ".2%"))
print(format(0.5, ".3%"))
# print(format(0.5, "%"))

print(format(8790645342, ","))

print(map(lambda val: val.swapcase(), ["Secret", "gARDEN", "GeNiUS"]))

large_number = (input("a large number "))
print(format(int(large_number), ","))
