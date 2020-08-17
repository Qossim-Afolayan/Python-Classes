def count_of_value(dictionary, integer):
    a = 0
    for key, value in dictionary.items():
        if value == integer:
            a += 1
            
    return a


my_dict = { "a" : 5, "b" : 3, "c" : 5 }

print(count_of_value(my_dict, 5))
print(count_of_value(my_dict, 2))

def sum_of_values(dictionary, lists):
    a = 0
    for key, value in dictionary.items():
        if key not in lists:
            continue
        else:
            a += value
            
    return a

my_dict = { "a": 5, "b": 3, "c": 10 }

print(sum_of_values(my_dict, ["a", "c"]))

lecture_attendees = [
    { "name": "Abdulfattah", "section": 400, "price paid": 99.99 },
    { "name": "Abdussamad", "section":200, "price paid": 149.99 },
    { "name": "Qossim", "section": 100, "price paid": 0.00}
]

for attendee in lecture_attendees:
    for key, value in attendee.items():
        print(f"The {key} is {value}")

# Assign a list of four dictionaries to a "complexity" variable below

# The first and third dictionaries should have two key-value pairs
# For those dictionaries, the keys should be strings and the values should be Booleans

# The second and fourth dictionaries should have three key-value pairs
# For those dictionaries, the keys shoulds be floats and the values should be list of strings. 
# The lists can be of any length.

complexity = [
    { "Qossim": True, "Python": True },
    { 2.34: ["2", "3", "4"], 4.86: ["4", "8", "6"], 7.24: ["7", "2", 4] },
    { "Sushi": False, "C++": False },
    { 5.64: ["5", "6"], 2.5: ["2", "5"], 3.4: ["3", "4"] }
]
