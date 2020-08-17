a = None
print(type(a))

def subtract(a, b):
    print(a - b)

result = subtract(3, 4)
print(result)

c = 19
print(type(c))

def find_my_letter(str, c):
    if c in str:
        return str.index(c)
    else:
        return -1

print(find_my_letter("dangerous", "a"))
print(find_my_letter("bazooka", "z"))
print(find_my_letter("lollipop", "z"))

def vowel_count(str):
    return str.count("a") + str.count("e") + str.count("i") + str.count("o") + str.count("u")

print(vowel_count("estate"))
print(vowel_count("helicopter"))
print(vowel_count("ssh"))

print("a" "b" "c")
#Escape characters
some_random_number = 5 
some_obscure_calculation = 25 
some_additional_statistic_fetched_from_somewhere = 10

final = some_random_number + \
        some_obscure_calculation + \
        some_additional_statistic_fetched_from_somewhere

print(some_random_number,     
some_obscure_calculation,     
some_additional_statistic_fetched_from_somewhere)
print("    content   ".strip())