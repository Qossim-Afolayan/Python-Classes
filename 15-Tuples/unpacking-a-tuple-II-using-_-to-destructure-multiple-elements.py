employee = ("Bob", "Johnson", "Manager", 50)

first_name, last_name, *details = employee
print(first_name)
print(last_name)
print(details)

*names, position, age = employee
print(position)
print(names)
print(age)

first_name, *details, age = employee
print(first_name)
print(details)
print(age)

first_name, last_name, position, *age = employee
print(employee)
print(first_name)
print(last_name)
print(position)
print(age)

print(first_name, last_name, position, *age)


# def sum_of_evens_and_odds(numbers):
#     sum1 = 0
#     sum2 = 0
#     for number in numbers:
#         if number % 2 == 0:
#             sum1 += number
#         else:
#             sum2 += number
            
#     return sum1,sum2

def sum_of_evens_and_odds(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    return (sum(even_numbers), sum(odd_numbers))

print(sum_of_evens_and_odds((2, 4, 6)))
print(sum_of_evens_and_odds((1, 3, 5)))
print(sum_of_evens_and_odds((1, 2, 3, 4)))