def add(a, b):
    pass
#Positional Argument are argument passed 
# add(4, -6)

# #Keyword Argument are argument that are attached to their parameters explicitly
# add(a = 4, b = -6)
def add(a, b, c):
    print("The sum of the three numbers is", a + b + c)

add(4, 5, 6)
add(a = 4, b = 5, c = 6)
add(4, b = 5, c =6)
add(4, c = 6, b = 5)
