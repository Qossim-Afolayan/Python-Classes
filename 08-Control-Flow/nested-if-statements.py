ingredient1 = "Pizza"
ingredient2 = "Meatballs"

if ingredient1 == "Pasta":
    if ingredient2 == "Meatballs":
        print("I recommend making Pasta and Meatballs")
    else:
        print("I recommend making plain Pasta")
else:
    print("I have no recommendation")

if ingredient1 == "Pasta" and ingredient2 == "Meatball":
        print("I recommend making Pasta and Meatballs")
elif ingredient1 == "Pasta":
    print("I recommend making plain pasta")
else:
    print("I have no recommendation")


def divisible_by_three_and_four(number):
    if number % 3 == 0 and number % 4 == 0:
        return True
    else:
        return False
        
print(divisible_by_three_and_four(3))
print(divisible_by_three_and_four(4))
print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(18))
print(divisible_by_three_and_four(24))


