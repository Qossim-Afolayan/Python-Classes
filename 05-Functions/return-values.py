def add(a, b):
    return a + b
    print("This is nonsense")

#Return concludes a function just like a self terminating line

result = add(4, 5)
print(result)

def easy_money():
    return 100

result = easy_money()
print(result)

def best_food_ever():
    return "Sushi"

result = best_food_ever()
print(result)

def convert_to_currency(a):
    return "$" + str(a)

result = convert_to_currency(8)
print(result)

def long_word(str):
    if (len(str) > 7):
        return True
    else:
        return False

    
result = long_word("Qossim")
print(result)

# Define a same_first_and_last_letter function that accepts a string as an argument. 
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same_first_and_last_letter("runner")   => True
# same_first_and_last_letter("Runner")   => False
# same_first_and_last_letter("clock")    => False
# same_first_and_last_letter("q")        => True

def same_first_and_last_letter(a):
    if  a[0] == a[-1]:
        return True
    else:
        return False
        
d = (same_first_and_last_letter("runner"))
e = (same_first_and_last_letter("Runner"))
f = (same_first_and_last_letter("clock"))
g = (same_first_and_last_letter("q"))
    
print(d)
print(e)
print(f)
print(g)
# Define a three_number_sum function that accepts a 3-character string as an argument. 
# The function should add up the sum of the digits of the string. 
# HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.
#
# EXAMPLES:
# three_number_sum("123")   => 6
# three_number_sum("567")   => 18
# three_number_sum("444")   => 12
# three_number_sum("000")   => 0


def three_number_sum(str):
    return (int(str[0]) + int(str[1]) + int(str[2]))
    
t = three_number_sum("456")
print(t)