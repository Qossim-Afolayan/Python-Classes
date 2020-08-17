# def reverse(str):
#     start_index = 0
#     last_index = len(str) - 1
#     reversed_string = ""

#     while last_index >= start_index:
#         reversed_string += str[last_index]
#         last_index -= 1

#     return reversed_string

# def reverse(str):
#     if len(str) <= 1:
#         return str

#     return str[-1] + reverse(str[:-1])



# def sum_of_lengths(strings):
#     for string in strings:
#         return len(string)

    

# #print(reverse("straw"))
# print(sum_of_lengths(["Hello", "Bob"]))

#straw 
# w + reverse(stra)
# w + a + reverse(str)
# w + a + r + reverse(st)


# def factorial(num):
#     if num == 1:
#         return num

#     return num * factorial(num - 1)


# print(factorial(4))






# 5 factorial is 5 * 4 * 3 * 2 * 1 = 120

# def reverse(str):
#     if len(str) <= 1:
#         return str
    
        
#     return str[-1] + reverse(str[:-1])

# print(reverse("Straw"))

# def factorial(number):
#     if number == 1:
#         return number


#     return number * factorial(number-1)
# print(factorial(6))

# def addition(string):
#     if len(string) == 1:
#         return string

#     return int(string[-1]) + int(addition(string[:-1]))



# print(addition("113"))


# def is_long(list):
#     if len(list) > 2:
#         return True
    
#     return False

# print(is_long(["a", 6, "afde"]))

def add(strings):
    if len(strings) == 1:
        return strings

    return strings[-1] + str(add(strings[:-1]))


print(add(["a", "6", "afde"]))

# def split_in_two(lists, num):
#     if num % 2 == 0:
#         return lists[2:]

#     return lists[:2]
# print(split_in_two(["a", "b", "c", "d", "e", "f"], 8))

def nested_extraction(list, index):
    if len(list):
        return list[index][index]

nl = [[3, 4, 5], [6, 7, 8], [9, 10,11]]

print(nested_extraction(nl, 2))

def beginning_and_end(elements):
    if elements[0] == elements[-1]:
        return True 

    return False

print(beginning_and_end([1, 2, 3, 4, 1]))

def long_word_in_collection(lists, string):
    if string in lists and len(string) > 4:
        return True

    return False

def sum_of_lengths(strings):
    total = 0
    for string in strings:
        total += int(string)
    return total

print(sum_of_lengths("12"))

values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]

# def odd_sum(numbers):
#     summ = 0
#     for number in numbers:
#         if number % 2 != 0:
#             summ += number
#     return summ



# print(odd_sum(values))

def greatest_number(numbers):
    summ = numbers[0]
    for number in numbers:
        if number < summ:
            summ = number

    return summ

print(greatest_number([4, 2, 6]))
print(greatest_number([-3, -2, -6]))

def concatenate(strings):
    conc = ""
    for string in strings:
        if len(string) > 2:
            conc += string

    return conc

print(concatenate(["Qossim", "Afolayan"]))
print(concatenate(["abc", "def", "gh"]))

def super_sum(lists):
    total = 0
    for list in lists:
        if 's' in list:
            total += list.find('s')

    return total
print(super_sum(["mustache", "greatest"]))
print(super_sum([]))
