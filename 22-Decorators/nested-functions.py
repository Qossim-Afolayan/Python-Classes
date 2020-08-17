#Gallons to cups 

# 1 gallon = 4 quarts 
# 1 quart = 2 pints 
# 1 pint = 2 cups

def convert_gallons_cup(gallons):
    def convert_gallons_quarts(gallons):
        print(f"Converting {gallons} to quarts!")
        return gallons * 4

    def conver_quarts_pints(quarts):
        print(f"Converting {quarts} to pints!")
        return quarts * 2

    def convert_pints_cups(pints):
        print(f"Converting {pints} to cups!")
        return pints * 2

    quarts = convert_gallons_quarts(gallons)
    pints = conver_quarts_pints(quarts)
    cups = convert_pints_cups(pints)
    return cups

print(convert_gallons_cup(4))
print(convert_gallons_cup(5))
