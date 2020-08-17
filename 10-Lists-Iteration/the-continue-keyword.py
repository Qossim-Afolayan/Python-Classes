# def sum_of_positive_numbers(values):
#     total = 0

#     for value in values:
#         if value > 0:
#             total += value
#     return total

# print(sum_of_positive_numbers([-1, 2, -3, 4, -3, 3, -8]))

# def sum_of_positive_numbers(values):
#     total = 0
#     for value in values:
#         if value < 0:
#             continue
#         total += value


#     return total

# print(sum_of_positive_numbers([-1, 2, -3, 4, -3, 3, -8]

for index, num in enumerate([1, 1, 2, 2, 5]):
    if index > num:
        break
    print(num)


# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# EXAMPLES
# length_match(["cat", "dog", "kangaroo", "mouse"], 3))  => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5))  => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4))  => 0
# length_match([], 5))                                   => 0

def length_match(strings, integer):
    total = 0
    for string in strings:
        if len(string) == integer:
            total += 1

    return total

# def length_match(strings, int):
#     total = 0
#     for string in strings:
#         if len(string) != int:
#             continue
#         total += 1

    # return total

print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))
print(length_match([], 5))


# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).

# def sum_from(num1, num2):
#     summ = 0
#     for num in range(num1, num2 + 1):
#         summ += num

#     return summ
# EXAMPLES
# sum_from(1, 2)   # 1 + 2                  => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5      => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8  => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12       => 42
def sum_from(num1, num2):
    total = 0
    for number in range(num1, num2 + 1):
        total += number
    return total
        
        

print(sum_from(1, 5))
print(sum_from(9, 12))
    





# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# EXAMPLES
# same_index_values([1, 2, 3], [3, 2, 1])                         => [1]
# same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])   => [1, 3]

def same_index_values(lists1, lists2):
    result = []
    for index, list1 in enumerate(lists1):
        if list1 == lists2[index]:
            result.append(index)

    return result

        
print(same_index_values([1, 2, 3], [3, 2, 1]))


        

