from unittest.mock import Mock
from random import randint

def generate():
    return randint(1, 10)

call_me_maybe = Mock(return_value = 26, side_effect = generate)

# call_me_maybe.side_effect = generate
print(call_me_maybe())
print(call_me_maybe())
print(call_me_maybe())

three_item_list = Mock()
three_item_list.pop.side_effect = [3, 2, 1, IndexError("pop from empty list")]

print(three_item_list.pop())
print(three_item_list.pop())
print(three_item_list.pop())
# print(three_item_list.pop())

mock = Mock(side_effect = NameError("Some error message"))
mock.side_effect = None
print(mock())

# Let's mock a fake Airport object.
# Create a Mock object and assign it to a variable called 'airport'. 

# The airport mock should have a 'gates' attribute set to a list of the strings “A1”, “B2”, and “C3”.

# The airport mock should have a 'departures' attribute set to a dictionary where 
# the keys are strings representing cities and the 
# values are strings representating their departure times.

# {
#   "Atlanta": "12:00PM",
#   "Nashville": "04:30PM"
# }

# The airport mock should have a 'close' attribute that is callable (i.e. an instance method). 
# When invoked, it should return the string “Closing”.

# The airport should have an 'open' attribute that is callable (i.e. an instance method). .
# When invoked the first time, it should return “Opening…”. 
# When invoked the second time, it should return “Already open”.

# EXAMPLE
#
# Given an airport Mock...
#
# print(airport.gates)      # ["A1", "B2", "C3"]
# print(airport.departures) # { "Atlanta": "12:00PM", "Nashville": "04:30PM" }
# print(airport.close())    # Closing
# print(airport.open())     # Opening...
# print(airport.open())     # Already open

# from unittest.mock import Mock

airport = Mock()

airport.gates = ["A1", "B2", "C3"],
airport.departures = {
    "Atlanta": "12:00PM",
    "Nashville": "04:30PM"
}


airport.close = Mock(return_value = "Closing")
airport.open.side_effect = ["Opening...". "Already open"]

print(airport.gates)      # ["A1", "B2", "C3"]
print(airport.departures) # { "Atlanta": "12:00PM", "Nashville": "04:30PM" }
print(airport.close())    # Closing

airport.open = state
print(airport.open())     # Opening...
print(airport.open())     # Already open