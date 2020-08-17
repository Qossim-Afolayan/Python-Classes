class Guitar():
    def __init__(self, wood):
        self.wood = wood



acoustic = Guitar("Alder")
electric = Guitar("Mahogany")

print(acoustic.wood)
print(electric.wood)

baritone = Guitar("Alder")
print(baritone.wood)

print(acoustic)
print(baritone)

a = [1, 2, 3]
b = [1, 2, 3]

class Musical():
    def __init__(self, name):
        self.name = name
        
        
rent = Musical("Rent")
mormon = Musical("Book of Mormon")
chicago = Musical("Chicago")

#Declare a Skyscraper class that accepts name and year parameters. 

# In the initialization process for an object, assign the name parameter to a name attribute 
# and the year parameter to a year attribute.

# Instantiate a Skyscraper object with the name “Empire State Building”  and the year 1931. 
# Assign it to a “empire" variable.

# Instantiate a Skyscraper object with the name “One World Trade Center” and the year 2014. 
class Skyscraper():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
empire = Skyscraper("Empire State Building", 1931)
wtc = Skyscraper("One World Trade Center", 2014)

# Assign it to a “wtc" variable.

# Declare a Zombie class that accepts health and brains_eaten parameters. 

# In the initialization process for a Zombie object, assign the 
# two parameters to two attributes with the same name.
#
# If the instantiation does not pass a health parameter, 
# it should be assigned a default value of 100.
#
# If the instantiation does not pass a brains_eaten parameter, 
# it should be assigned a default value of 5.

# Instantiate a Zombie object with 80 health and 5 brains eaten. 
# Assign it to a “bob” variable.
#
# Instantiate a Zombie object with 120 health and 3 brains eaten.
# Assign it to a “sally” variable.
#
# Instantiate a Zombie object with no custom parameters.
# Assign it to a “benjamin” variable.
#
# Practice instantiating the objects with both positional and keyword arguments
class Zombie():
    def __init__(self, health = 100, brains_eaten = 5):
        self.health = health
        self.brains_eaten = brains_eaten

bob = Zombie(80)
sally = Zombie(120, 3)
benjamin = Zombie()

print(benjamin.health)