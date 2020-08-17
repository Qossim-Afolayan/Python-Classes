salutation = "Mr. Kermit is a Frog"
#startswith and endswith method returns a boolean
print(salutation.startswith("M"))
print(salutation.startswith("Mr"))
print(salutation.startswith("Mr."))
print(salutation.startswith("m"))
print(salutation.startswith("mr."))
print(salutation.startswith("ker"))

print()
print(salutation.endswith("g"))
print(salutation.endswith("og"))
print(salutation.endswith("Frog"))
print(salutation.endswith("frog"))
print(salutation.endswith("a Frogg"))

def check(a):
    if a.count("?") > 3:
        return True
    else: 
        return False

print(check("What's your name????"))

# mad_libs = "{name} laughed at the {adjective} {noun}."
# name = input("Enter your name! ")
# adjective = input("Enter an adjective! ")
# noun = input("Enter a noun! ")

#print(mad_libs.format(name = name, adjective = adjective, noun = noun))

def three_digit_number(str):
    return finput("Enter a three-digit-number!{str}")

print(int(str[0]) + int(str[1]) + int(str[2]))


