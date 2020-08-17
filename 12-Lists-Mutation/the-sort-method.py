temperatures = [40, 23, 36, 66, 46]
temperatures.sort()
temperatures.reverse()
print(temperatures)

coffees = ["Latte", "Expressor", "Machiato", "Fapruccino"]
coffees.sort()
coffees.reverse()
print(coffees)

coffees = ["Latte", "expressor", "machiato", "Fapruccino"]
coffees.sort()
coffees.reverse()
print(coffees)

# Sorted function returns a new list and do not mutate the original list
coffees = ["Latte", "expressor", "machiato", "Fapruccino"]
print(sorted(coffees))
sorted(coffees).reverse()

songs = ["Proven", "Perseverance", "Defeatist", "Puritan"]
songs[1:3] = ["I Will Be Heard"]
numbers = [1, 4, 5, 7, 9]


numbers[1:3] = [6, 8]

print(numbers)



