#A  dictionary is an unordered data structure for declaring relationships(mappings) between objects 

#A mutable data structure consisting of pairs of keys and values 
# a key is an object6 that serves as a unique identifier for a value (unique) - immutable
# a value is any python object (duplicates) - any data type

ice_cream_preferences = {
    "Benjamin": "Chocolate",
    "Qossim": "Vanilla",
    "Abdurrahman": "Cookies & Creme",
    "Abdussamad": "Chocolate"
}

print(len(ice_cream_preferences))

flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295
}

print(flight_prices["Chicago"])
print(flight_prices["San Francisco"])
#print(flight_prices["Seatle"]) #Key error#

gym_membership_packages = {
    29: ["Machines"],
    79: ["Machines", "Vitamins Suplements"],
    120: ["Machines", "Vitamins Suplements", "Sauna"]
}
print(gym_membership_packages[29])
print(gym_membership_packages[120])

print(gym_membership_packages.get(29, ['Basic Dumbells']))
print(gym_membership_packages.get(100, ['Basic Dumbells']))
#get method allows you to access a value and doesnt allow your code to crash



