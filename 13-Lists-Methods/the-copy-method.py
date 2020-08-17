units = ["meter", "kilogram", "second", "ampere", "Kelvin", "Candela", "mole"]

more_units = units.copy()

# print(units)
# print(more_units)
units.remove("kilogram")

print(units)
print(more_units)

even_more_units = units[:]
print(even_more_units)