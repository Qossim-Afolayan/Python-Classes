users = "Bob, Dave, John, Sun, Randy, Meg"

print(users.split(", "))

print(users.split(", ", 3))

sentence = "I am learning how to code"
words = sentence.split(" ")
print(words)


def word_lengths(string):
    list = string.split(" ")
    lengths = []
    for value in list:
        lengths.append(len(value))

    return lengths


print(word_lengths("Mary Poppins was a nanny"))
print(word_lengths("Somebody stole my donut"))

def cleanup(strings):
    cleaned = []
    for string in strings:
        if string == " " or string == "":
            continue
        else:
            cleaned.append(string)
            
            
    return " ".join(cleaned)

print(cleanup(["", "", " "]))
print(cleanup(["cat", " ", "er", "", "pillar"]))

print(" ".join(["cat", "er", "pillar"])


# Uncomment the commented lines of code below and complete the list comprehension logic

# The floats variable should store the floating point values
# for each string in the values list.
# values = ["3.14", "9.99", "567.324", "5.678"]
# floats = [float(value) for value in values]
# print(floats)

# The letters variable should store a list of 5 strings.
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
# name = "Boris"
# letters = [name.split(", ") * 3 for char in name]
# print(letters)

# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
# elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
# lengths = [len(element) for element in elements]
# print(lengths)

# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]


# def destroy_elements(lists1, lists2):
#     result = []
#     for index, list1 in enumerate(lists1):
#             if lists2[index] not in lists1:
#                 result.append(lists2[index])

#     return result

# print(destroy_elements([1, 2, 3], [1, 2]))

