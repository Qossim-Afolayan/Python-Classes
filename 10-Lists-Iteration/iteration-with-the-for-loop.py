#An object is interable if its element can be stepped through one by one

dinner = "Steak and Potatoes"

# for character in dinner:
#     print(character)

numbers = [2, 3, 4, 5, 6]
for number in numbers:
    print(number * number)


novelists = ["Fitzgerald", "Heningway", "Steinback"]
for novelist in novelists:
    print(len(novelist))

print(novelist)
print(number)

total = 0

for number in numbers:
    total += number

print(total)


# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# EXAMPLES
# sum_of_lengths(["Hello", "Bob"])                  => 8
# sum_of_lengths(["Nonsense"])                      => 8
# sum_of_lengths(["Nonsense", "or", "confidence"])
# initial = 0
# def sum_of_lengths(strings):
#     L = [len(string) for string in strings]
#     return sum(L)
#     # for string in strings:
#     #     if len(strings) == 1:
#     #         return len(strings)

#         #return (len(strings[-1])) + (len(sum_of_lengths(strings[:-1])))
# print(sum_of_lengths(["Hello", "Bob"]))
# #     return int(str[-1]) + int(addition(str[:-1]))

#   => 20

def sum_of_lengths(strings):
    initial = 0
    for (string) in strings:
        initial = initial + len(string)
    return initial

print(sum_of_lengths(["Hello", "Bob"]))
    

    

#print(reverse("straw"))



# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# EXAMPLES
# product([1, 2, 3])     => 6
# product([4, 5, 6, 7])  => 840
# product([10])          => 10

def product(numbers):
    result = 1
    for x in numbers:
        result = result * x
    return result


print(product([1, 2, 3]))
