#other boolean type
print(5 < 8) #True
print(8 < 5) #False
print(8 <= 10)#True
print(9 <= 7)#false
print(8 < 9 <= 15)#True
print(4 < 6 <= 5)#false

print(9 > 6)#True
print(4 > 6)#false
print(4 >= 3)#True
print(5 >= 7)#False
print(3 > 2 >= 2)#True
print(3 > 2 >= 5)#False

print("""Hello
my name is 
Boris
""")
def first_longer_than_second(str, word):
    return len(str) > len(word)
    
result = first_longer_than_second("Ruby", "Python")
print(result)




