# 0 is falsy and every other value is truthy
if 3:
    print("Hello")

if 0:
    print("Nice")


if -3:
    print("Goodbye")

#An empty string is falsy
if "":
    print("Hello")

if "Nice":
    print("purchase")

print(bool(1))
print(bool(0))
print(bool(""))
print(bool(3.14))
print(bool(-1.24466))
print(bool(0.0))


def even_or_odd(int):
    if (int % 2 == 0):
        return "even"
    else:
        return "odd"

print(even_or_odd(7))


# def truthy_or_falsy(a):
#     if (a):
#         return "The value" +" "+ str(a) + " is truthy"
#     else:
#         return "The value" + " "+ str(a) + " is falsy"

# print(truthy_or_falsy(8))
# print(truthy_or_falsy(0))

# print("The value str(8)", 8, "is truthy")

def truthy_or_falsy(a):
    if(a):
        return f"The value {a} is truthy"
    
    return f"The value {a} is falsy"

print(truthy_or_falsy(8))

print(bool("  "))








