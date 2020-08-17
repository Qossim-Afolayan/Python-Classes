capitals = {
    "New York": "Albany",
    "California": "Sacremento",
    "Texas": "Austin"
}

inverted = { capital: state for state, capital in capitals.items() if len(state) != len(capital)}
print(inverted)
prices = {
    "Big Mac": 3.99,
    "French Fries": 0.99,
    "Soda": 0.99
}

calories = {
    "Big Mac": 600,
    "French Fries":300,
    "Soda": 200
}

print({meal: calories[meal] for meal, price in prices.items() if price < 1})

sentences = [
    "Bobby went to the store on the corner",
    "Sally ater a candy bar",
    "Justin played on his deluxe piano"
]

word_counts = {sentence:len(sentence.split(" ")) for sentence in sentences }
print(word_counts)

values = [1, 2, 3, 4, 5]
print({ value: sum(values[: index + 2]) for index, value in enumerate(values)})

# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
# channels = {
#   2: "CBS",
#   4: "NBC",
#   5: "FOX",
#   7: "ABC"
# }
# The stations_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers
#
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}

def stations_to_numbers(dictionary):
    return { value: key for key, value in dictionary.items()}

channels = {
  2: "CBS",
  4: "NBC",
  5: "FOX",
  7: "ABC"
}
print(stations_to_numbers(channels))


# Declare a coaster_conversion function that accepts a dictionary
# The keys of the dictionary will be strings representing roller coasters
# The values will be the heights of each coaster in meters
#
# Return a new dictionary with the same keys.
# The values should be the heights converted from meters to feet,
# The final values (in feet) should also be rounded to the closest integer
# HINT: 1 meter is equal to 3.28084 feet
# HINT: The round function rounds a number to the nearest integer
#
# coasters = {
#   "Kingda Ka": 139,
#   "Top Thrill Dragster": 130,
#   "Superman: Escape From Krypton": 126
# }
#
# coaster_conversion(coasters) => 
# {'Kingda Ka': 456, 'Top Thrill Dragster': 426, 'Superman: Escape From Krypton': 413}

def coaster_conversion(my_dict):
    return { coaster: round(height * 3.28084) for coaster, height in my_dict.items() }

coasters = {
  "Kingda Ka": 139,
  "Top Thrill Dragster": 130,
  "Superman: Escape From Krypton": 126
}

print(coaster_conversion(coasters))
numbers = [3, 6, 7, 12, 15]
my_diction = { number: number**3 for number in numbers if number % 2 == 0 }

print(my_diction) 
