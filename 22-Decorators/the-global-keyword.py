# x = 10

def change_stuff():
    global x
    x = 15 

# print(x)
change_stuff()
print(x)

a = 1
def modify_a(b):
    global a
    a = b
    return a

print(modify_a(5))