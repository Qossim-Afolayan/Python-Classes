errands = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]

print(enumerate(errands))

for index, errand in enumerate(errands):
    print(f"{errand} is number {index} on my list of things to do today!")

for index, errand in enumerate(errands):
    print(f"{errand} is number {index + 1} on my list of things to do today!")

for index, errand in enumerate(errands, 1):
    print(f"{errand} is number {index} on my list of things to do today!")

#To keep track of the index position and the element itself

#Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
# def in_list(lists, word):
#     for idx, list in enumerate(lists):
#         if list == word:
#             return idx

#     return -1
# EXAMPLES
strings = ["enchanted", "sparks fly", "long live"]
# print(in_list(strings, "enchanted")) 
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1
def in_list(lists, string):
    for index, list in enumerate(lists):
        if list == string:
            return index
        
    return -1
        
    
        
            
        
# strings = ["enchanted", "sparks fly", "long live"]
print(in_list(strings, "enchanted"))
print(in_list(strings, "fifteen"))
print(in_list(strings, "sparks fly"))

# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.

def sum_of_values_and_indices(numbers):
    total = 0
    for index, number in enumerate(numbers):
        total += number + index

    return total
# EXAMPLES
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0

def sum_of_values_and_indices(numbers):
    total = 0
    for idx, number in enumerate(numbers):
        total += idx + number
        
            
    return total
    
        

print(sum_of_values_and_indices([1, 2, 3]))