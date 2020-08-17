#not keyword to negate an expression

print(not True)
print(not False)

if "H" in "Hello":
    print("The character exist")
if "Z" not in "Hello":
    print("That character does not exist")

value = 10
if value > 100:
    print("This will not print")
if value < 100:
    print("The will print")
if not value > 100:
    print("This will print!")