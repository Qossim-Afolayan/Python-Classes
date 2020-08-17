#Control Flow is the order in which individual statements, instructions, or functions calls of a program are executed.

handsome = True
admin = False

print(2 < 4)
print(7 >= 8)
result = 2 < 4
print(result)


print("xbox" == "xbox")
print("xbox" == "playstation")
print("xbox" == "Xbox")
print(5 == 5)
print (5 == 7)

print(4 != 5)
print(4 != 4 )
print("Qossim" != "Qossim")
print("Qossim" != "qossim")
print(True != False)
print(True != True) 

def truthy_or_falsy(a):
    if (a):
        return f"The value {a} is truthy"

    return f"The value {a} is falsy"

print(truthy_or_falsy(0))
print(truthy_or_falsy(5))


def even_or_odd(integer):
    if (integer % 2 == 0):
        return "even"

    return "odd"

print(even_or_odd(7))
print(even_or_odd(100))
