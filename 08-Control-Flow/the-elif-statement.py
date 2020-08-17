#elif to add another condition after an if statement
def positive_or_Negative(a):
    if a > 0:
        return "Positive!"
    elif a < 0:
        return "Negative!"
    elif a == 0:
        return "Neither! it's zero"

print(positive_or_Negative(5))
print(positive_or_Negative(-3))
print(positive_or_Negative(0))

def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "divide":
        return a / b 
    elif operation == "multiply":
        return a * b
    else:
        return "I don't know what you want me to do"
print(calculator("add", 8, 5))
print(calculator("subtract", 8, 5))
print(calculator("divide", 8, 5))
print(calculator("multiply", 8, 5))
print(calculator("transmogrify", 8, 5))
print(calculator("", 8, 5))

def negative_energy(a):
    if a > 0:
        return a - 0
    else:
        return 0 - a
        
print(negative_energy(-5))

