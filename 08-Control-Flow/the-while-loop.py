#interation : repetation
#Loop is a series of instruction that is repeated
#While loop continues to repeat while the condition is correct
#infinite loop is a loop that never ends 

# count = 0

# while count <= 5:
#     print(count)
#     count += 1

# print(count)

# count = 0

# while count <= 5:
#     print(count)
#     count += 1

# invalid_number = True

# while invalid_number:
#     user_value = int(input("Enter a number above 10: "))
#     if user_value > 10:
#         print(f"Thanks, that works! {user_value} is a great choice")
#         invalid_number = False
#     else:
#         print("That doesn't fit! Try again!")

def  fizzbuzz(n):
    i = 0
    while i < n:
        i += 1
        if (i % 3 == 0 and i % 5 == 0):
            print("Fizzbuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)

        

fizzbuzz(30)
         
def fizzbuzz(final_number):
  current_number = 1
  while current_number <= final_number:
    if current_number % 15 == 0:
      print("FizzBuzz")
    elif current_number % 3 == 0:
      print("Fizz")
    elif current_number % 5 == 0:
      print("Buzz")
    else:
      print(current_number)
    current_number += 1

fizzbuzz(30)