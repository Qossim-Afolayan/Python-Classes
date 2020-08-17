print("programming"[1:4])


muscles = ["Biceps", "Triceps", "Detroit", "Santarious"]

print(muscles[1:3])
print(muscles[1:2])

print(muscles[0:2])
print(muscles[:3])
print(muscles[2:100])
print(muscles[2:])

print(muscles[-4:-2])
print(muscles[-3:])
print(muscles[:-1])
print(muscles[1:-1])

print(muscles[::2])
print(muscles[::-2])
print(muscles[::-1])


def split_in_two(list, number):
    if number % 2 == 0:
        return list[3:]
    return list[0:2]

values = ["a", "b", "c", "d", "e", "f"]
print(split_in_two(values, 3))

# Declare a nested_extraction function that accepts \
# a list of lists and an index position.
#
# The function should use the index as the basis of finding both the nested list 
# and the element from that list with the given index position
#
# You can assume the number of lists will always be equal to 
# the number of elements within each of them.
#
# nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
# nested_extraction(nl, 0)  => 3
# nested_extraction(nl, 1)  => 8
# nested_extraction(nl, 2)  => 12

def nested_extraction(lists, index):
    return lists[index][index]

nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
print(nested_extraction(nl, 0))
print(nested_extraction(nl, 1))
print(nested_extraction(nl, 2))




# Declare a beginning_and_end function that accepts a list of elements.
#
# It should return True if the first and last elements in the list are equal and False if they are unequal.
#
# Assume the list will always have at least 1 element.
#
# beginning_and_end([1, 2, 3, 1])     => True
# beginning_and_end([1, 2, 3, 4, 5])  => False
# beginning_and_end(["a", "b", "a"])  => True
# beginning_and_end([15])             => True

def beginning_and_end(list):
    if list[0] == list[-1]:
        return True
    return False

print(beginning_and_end([1, 2, 3, 1]))
print(beginning_and_end([1, 2, 3, 4, 5]))




# Declare a long_word_in_collection function that accepts a list and a string. 
# The function should return True if 
#   - the string exists in the list AND
#   - the string has more than 4 characters.
#
# words = ["cat", "dog", "rhino"]
# long_word_in_collection(words, "rhino")  => True
# long_word_in_collection(words, "cat")    => False
# long_word_in_collection(words, "monkey") => False

def long_word_in_collection(array,string):
    if string in array and len(string) > 4:
        return True
    return False

words = ["cat", "dog", "rhino"]
print(long_word_in_collection(words, "rhino"))
# long_word_in_collection(words, "cat")    => False
# long_word_in_collection(words, "monkey") => False





