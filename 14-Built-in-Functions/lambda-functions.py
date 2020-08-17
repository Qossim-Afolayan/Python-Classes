metals = ["gold", "silver", "platinum", "palladium"]

print(list(filter(lambda metal: len(metal) > 5, metals)))
print(list(filter(lambda metal: "p" in metal, metals)))

#lambda : hidden function

print(list(map(lambda word: word.count("l"), metals)))
print(list(map(lambda word: word.replace("s", "$"), metals)))

# def destroy_elements(lists1, lists2):
#     result = []
#     for list1 in lists1:
#         if list1 not in lists2:
#             result.append(list1)

#     return result

def destroy_elements(lists1, lists2):
    # return list(filter(lambda list1: list1 not in lists2, lists1))
    return [list1 for list1 in lists1 if list1 not in lists2]
    

print(destroy_elements([1, 2, 3], [1, 2]))


#Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#
# EXAMPLES:
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3)     => ['cat', 'dog', 'ace']
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5)     => ['heart']
# right_words([], 4)                                         => []

# def right_words(words, number):
#     result = []
#     for word in words:
#         if len(word) == number:
#             result.append(word)
#     return result

# print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))
def right_words(words, number):
    # return list(filter(lambda word: len(word) == number, words))
    return [word for word in words if len(word) == number]

print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))





# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#
# EXAMPLES:
# only_odds([1, 3, 5, 6, 7, 8])      =>  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])            =>  []
# def only_odds(wholes):
# 	total = []
# 	for whole in wholes:
# 		if whole % 2 != 0:
# 			total.append(whole)
			
# 	return total

def only_odds(wholes):
    # return list(filter(lambda whole: whole % 2 != 0, wholes))
    return [whole for whole in wholes if whole % 2 != 0]

print(only_odds([1, 3, 5, 6, 7, 8]))

# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# EXAMPLES:
# count_of_a(["alligator", "aardvark", "albatross"])    => [2, 3, 2]
# count_of_a(["plywood"])                               => [0]
# count_of_a([])                                        => []

# def count_of_a(strings):
# 	counts = []
# 	for string in strings:
# 		if len(string) >= 0:
# 			counts.append(string.count("a"))
			
# 	return counts

def count_of_a(strings):
    # return list(map(lambda string: string.count("a"), strings))
    return [string.count("a") for string in strings]

print(count_of_a(["plywood"]))