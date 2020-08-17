value = [3, 6, 9, 12, 15, 18, 21, 24]
other_value = [5, 10, 15, 20, 25, 30]

def odd_sum(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total += number
    return total

print(odd_sum(value))
print(odd_sum(other_value))

def greatest_number(numbers):
    greatest = 0
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print(greatest_number([4, 5, 9, 8]))
print(greatest_number([4, 3, 2, 1]))

# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.
#
# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

def smallest_number(smalls):
    smallest = smalls[0]
    for small in smalls:
        if small <= smallest:
            smallest = small
    return smallest

print(smallest_number([1, 2, 3]))
print(smallest_number([3, 2, 1]))


# Define a concatenate function that accepts a list of strings. 
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""

def concatenate(strings):
    conc = ""
    for string in strings:
        if len(string) > 2:
            conc += string

    return conc

print(concatenate(["ab", "cd", "ef", "gh"]))
print(concatenate(["abc", "de", "fgh", "ic"]))
print(concatenate(["abc", "def", "ghi"]))




# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter “s” in each word. 
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12
greeting = "Assalamuallaykum warahmatullah WabarakatuH Sir"
print(greeting.replace("Sir", "ma"))
browser = "Google Chrome"
print(browser.find(" ")) 

def super_sum(books):
    total = 0
    for book in books:
        if "s" in book:
            total += book.find("s")

    return total

print(super_sum(["mustache", "greatest", "almost"]))




