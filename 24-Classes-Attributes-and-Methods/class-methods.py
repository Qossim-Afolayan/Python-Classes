class SushiPlatter():
    def __init__(self, salmon, tuna, shrimp, squid):
        self.salmon = salmon
        self.tuna = tuna
        self.shrimp = shrimp
        self.squid = squid

    @classmethod
    def lunch_special_A(cls):
        return cls(salmon = 2, tuna = 4,  shrimp = 6, squid = 0)

    @classmethod
    def tuna_lover(cls):
        return cls(salmon = 0, tuna = 20, shrimp = 0, squid = 2)

qossim = SushiPlatter(salmon = 8, tuna = 9, shrimp = 2, squid = 3)
print(qossim.salmon)

lunch_eater = SushiPlatter.lunch_special_A()
print(lunch_eater.salmon)


tuna_fan = SushiPlatter.tuna_lover()
print(tuna_fan.tuna)

# Define a Chocolate class that accepts and assigns a cacao_content attribute.

# Define a "sweet" class method that returns a 
# Chocolate object with a cacao_content value of 30.

# Define a "semisweet" class method that returns a 
# Chocolate object with a cacao_content value of 50.

# Define a "bittersweet" class method that returns a 
# Chocolate object with a cacao_content value of 70.

# Define a "bitter" class method that returns a 
# Chocolate object with a cacao_content value of 99.

class Chocolate():
    def __init__(self, cacao_content):
        self.cacao_content = cacao_content


    @classmethod
    def sweet(cls):
        return cls(cacao_content = 30)

    @classmethod
    def semisweet(cls):
        return cls(cacao_content = 50)

    @classmethod
    def bittersweet(cls):
        return cls(cacao_content = 70)

    @classmethod
    def bitter(cls):
        return cls(cacao_content = 99)

choco = Chocolate.bitter()
print(choco.cacao_content)