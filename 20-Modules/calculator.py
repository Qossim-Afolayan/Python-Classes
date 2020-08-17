# a module is any python file with .py extension and used by other files 
#A script is a python file used directly 
#Name space is a container (protective walls)

creator = "Qossim"
PI = 3.14159

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def area(radius):
    return PI * radius * radius

_year = 2020

if __name__ == "_main_":
    print("This is will only run when calculator is being executed as a script")
    print(subtract(3, 5))
