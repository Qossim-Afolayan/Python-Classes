class Student():
    def __init__(self, maths, history, writing):
        self.maths = maths
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.maths + self.history + self.writing

    def __eq__(self, other_student):
        return self.grades == other_student.grades

    def __gt__(self, other_student):
        return self.grades > other_student.grades

    def __le__(self, other_student):
        return self.grades <= other_student.grades

    def __add__(self, other_student):
        return self.grades + other_student.grades

    def __sub__(self, other_student):
        return self.grades - other_student.grades

    
bob = Student(maths = 90, history = 90, writing = 90)
moe = Student(maths = 100, history = 80, writing = 90)
joe = Student(maths = 45, history = 50, writing = 40)
print(bob + moe)

# Part A: Instantiation

# Define a BusTrip class that is initialized with a destination, 
# a bus company, and a price for the trip. 
# Preserve the arguments as attributes on the object.
# The choice of whether to use protected attributes is up to you.



# Part B: String Representation

# The string representation of a BusTrip object must be a string in the form of:
#    "You paid 24.99 to Greyhound to go to Boston.""
# In this example, “Boston” is the destination, “Greyhound” is the bus company, and 24.99 is the price.
# These are all fed in as arguments when a BusTrip object is initialized.

# Part C: Equality

# Implement equality logic between two different BusTrip objects.
# Two BusTrips object are considered equal if:
#   -- they have the same destination
#   -- their price is within 3 dollars of each other
# HINT: Use Python’s abs function to calculate the absolute value of a number.

# Sample Execution
boston1 = BusTrip(destination = "Boston", company = "Greyhound", price = 24.99)
boston2 = BusTrip(destination = "Boston", company = "Megabus", price = 22.99)
boston3 = BusTrip(destination = "Boston", company = "Megabus", price = 49.99)
philly  = BusTrip(destination = "Philadelphia", company = "Peter Pan", price = 12.99)

print(boston1)            # You paid 24.99 to Greyhound to go to Boston.
print(boston1 == philly)  # False - different destinations
print(boston1 == boston2) # True - same destination and insignificant price difference
print(boston1 == boston3) # False - large price difference