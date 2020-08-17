# name, adjectives, noun
# mad_libs = "{name} laughed at the {adjective} {name}."

# # print(mad_libs.format(name = "Qossim", adjective = "Green", noun = "alien"))
# # print(mad_libs.format("She", "silly", "tomato"))
# name = input("Enter your name: ")
# adjective = input ("Enter an adjective: ")
# noun = input("Enter a noun: ")

# print(mad_libs.format(noun = noun, adjective = adjective, name = name)

# mad_libs = "{name} 



name = "Bobby"
adjective = "green"
noun = "alien"

mid_libs = f"{name} laughed at the {adjective} {noun}."
print(mid_libs)

print(F"2 + 2 is {2 + 2}")


def truthy_or_falsy(arg):
    if bool(arg) == False:
        return f"The value {arg} is falsy"
    else:
        return f"The valus {arg} is truthy"

print(truthy_or_falsy(8))

