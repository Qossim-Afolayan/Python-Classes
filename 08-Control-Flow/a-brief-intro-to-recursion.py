# zip_code = "900201"

# #check
# # if len(zip_code) == 5:
# #     check = "Valid"
# # else:
# #     check = "Invalid"

# # print(check)

# check = "Valid" if len(zip_code) == 5 else "Invalid"
# print(check)

# RECURSION is when a function calls itself
# def count_down_from(number):
#      start = number
#      while start > 0:
#          print(start)
#          start -= 1

# #BASE case condition to stop

# def count_down_from(number):
#     if number <= 0:
#         return #none

#     print(number)
#     count_down_from(number - 1)



# count_down_from(10)

# def reverse(str):
#     start_index = 0
#     last_index = len(str) - 1
#     reversed_string = ""

#     while last_index >= start_index:
#         reversed_string += str[last_index]
#         last_index -= 1

#     return reversed_string

def addition(str):
    if len(str) == 1:
        return str

    return int(str[-1]) + int(addition(str[:-1]))

print(addition("567185"))

# print(reverse("straw"))  
# #warts

def count_down_from(number):
    if number <= 0:
        return
    print(number)
    count_down_from(number - 1)

count_down_from(5)
# Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. 
# Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return 
#  result of a comparison.

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base: 
    # If number is equal to 1, it's a power (base**0).
    return
  elif number % base != 0:
    return False
  elif number == 1:
    return True 

  # Recursive case: keep dividing number by base.
  else:
    return True
  is_power_of(number/base, base)
  

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

#Q2:
# The count_users function recursively counts the amount of users that belong to a group in the company system, 
# by going through each of the members of a group and if one of them is a group, recursively calling the 
# function and counting the members. But it has a bug! Can you spot the problem and fix it?

def count_users(group):
  count = 0
  for member in group:
    count += 1
    if member == group:
      count += count_users(member)
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18


#Q3:
# Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1.
#  For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.

def sum_positive_numbers(n):
  if n == 1:
    return n
  
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
