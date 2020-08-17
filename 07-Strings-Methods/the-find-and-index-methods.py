#Method is a function thatacts upon a specific object
#methods can be involked 
#find methods returns the index position of the first occurrent of the substring

browser = "Google Chrome"

print(browser.find("C"))
print(browser.find("Ch"))
print(browser.find("o"))
print(browser.find("G"))
print(browser.find("z"))
print(browser.find("c"))
print(browser.find("r"))




print()
 
print(browser.find("o"))
print(browser.find("o", 2))
print(browser.find("o", 5))
print(browser.find("Ch"))

print("Ch" in browser)

print(browser.index("Ch"))
#print(browser.index("z"))

str = "It is a tecnical tutorial"
print(str.rfind("t"))

#rfind method finds a substring in a string and returns the highest index of all its occurence
adam = "He has so many diverged views"
print(adam.rfind("e")) #26
print(adam.rfind("s")) #28
print(adam.rfind("i")) #25
print(adam.rfind(" "))
print(len(""))

#When an argument that's not in the object is passed to the find, it returns a -1 while sn index method raise a value error




print(r"C:\news\travel")
# r = Raw 
word = "race" 
word += "car" 
print(word)

print("Let me help you add two numbers")
first_number = int(input("Enter your first number! "))
second_number = int(input("Enter your second number! "))

print(first_number + second_number)

print("Thanks!")


