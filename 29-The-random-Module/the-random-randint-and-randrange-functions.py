import random

print(random.random())

print(random.random() * 100)

print(random.randint(1, 10))

print(random.randrange(0, 50, 10))

#The choice and the sample function
print(random.choice(["Qossim", "Gbolahan", "Afolayan"]))
print(random.choice([1, 2, 3, 4]))

# a = (random.randint(0, 20))

# b = int(input("Guess a number between 1 and 20 "))
# if b < a:
#     print("Your guess is too low")
# elif b > a:
#     print("Your guess is too high")
# else:
#     print("Thumbs up!")
# print(F"The number is {a}")

import math
 # Taking Inputs
lower = int(input("Emter Lower bound:- ")) 
 
# Taking Inputs
upper = int(input("Enter Upper bound:- "))  
 
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower, 2))," chances to guess the integer!\n")
 
 # Initializing the number of guesses.
count = 0
 
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
     
     # taking guessing number as input
    guess = int(input("Guess a number:- ")) 
     
    # Condition testing
    if x == guess:  
       print("Congratulations you did it in ", count, " try")
       # Once guessed, loop will break 
       break
    elif x > guess:
       print("You guessed too small!")
    elif x < guess:
       print("You Guessed too high!")
 
# If Guessing is more than required guesses, 
# shows this output.
if count >= math.log(upper - lower + 1, 2):
   print("\nThe number is %d"%x)
   print("\tBetter Luck Next time!")


