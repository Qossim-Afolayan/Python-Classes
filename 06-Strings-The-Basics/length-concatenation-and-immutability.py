print(len("Python"))
print(len("Machine Language") > 7)
print(len("#$^"))
print(len(""))
print(len(" "))

# print(len(4))
# print(len(3.44))

print("Qossim" + "Afolayan")
print("Qossim " + "Afolayan")
print("Qossim" + " Afolayan")
print('Qossim' + " " + 'Afolayan')

print("a" "b" "c")
print("------" * 20)

print(type({ "NJ": "Trenton" }))

def long_word(b):
    if len(b) > 7:
        return True
    else:
        return False
    
result = long_word("Qossim")
print(result)

book = long_word("Seven Habits of Highly Effective Teens")
print(book)

def first_longer_than_second(v, u):
    if len(v) > len(u):
        return True
    else:
        return False
    
result = first_longer_than_second("Qossim", "Afolayan")
print(result)

Food = long_word("Kilimanjaro")
print(Food)