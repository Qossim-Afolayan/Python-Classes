# Conditional logic Evaluate to booleans 
#Block is a set of codes that belong together as a group
#Blocks are detected by indentations (def)

if 5 > 3:
    print("Yep, That's true. This would be printed!")
    print("Hooray")


if 6 > 10:
    print("Nope, This would not be print")


if "boris" == "boris":
    print("Great name")

if "Qossim" != "qossim":
    print("Nice name")

if True:
    print("Always true, always print")

if False:
    print("Never true, not fit to print")
    
def fizzbuzz(i):
    n=1
    while n<=i:
        if n%3==0 and n%5==0:
            print("FizzBuzz")
        elif n%3==0:
            print("Fizz")
        elif n%5==0:
            print("Buzz")
        else:
            print(n)
        n+=1

fizzbuzz(30)




