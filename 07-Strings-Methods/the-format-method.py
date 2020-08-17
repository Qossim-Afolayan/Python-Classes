#format method to inject, interpolate a dynamic value (variables)into an existing string
# name, adjectives, noun
#Argument with relative position
# mad_libs = "{} laughed at the {} {}."

# print(mad_libs.format("Qossim", "Green", "alien"))
# print(mad_libs.format("She", "silly", "tomato"))

# #Argument with numeric position
# mad_libs = "{2} laughed at the {1} {0}."

# print(mad_libs.format("Qossim", "Green", "alien"))
# print(mad_libs.format("She", "silly", "tomato"))

# #Argument with  keyword parameter
mad_libs = "{name} laughed at the {adjective} {name}."

# print(mad_libs.format(name = "Qossim", adjective = "Green", noun = "alien"))
# print(mad_libs.format("She", "silly", "tomato"))
name = input("Enter your name: ")
adjective = input ("Enter an adjective: ")
noun = input("Enter a noun: ")

print(mad_libs.format(noun = noun, adjective = adjective, name = name)
