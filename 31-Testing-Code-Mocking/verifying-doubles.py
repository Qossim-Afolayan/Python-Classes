from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Qossim's Burritos" #class attribute

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)

    def __init__(self, protein, rice, guacamole_portion):
        self.protein = protein
        self.rice = rice
        self.guacamole_portion = guacamole_portion

    def add_guac(self):
        self.guacamole_portion += 1

lunch = BurritoBowl.steak_special()
print(lunch.protein)
lunch.add_guac()
print(lunch.guacamole_portion)

class_mock = MagicMock(spec = BurritoBowl)
print(class_mock.restaurant_name)
print(class_mock.steak_special())
# print(class_mock.chicken_special)
# print(class_mock.city())
class_mock.delicious = True
print(class_mock.delicious)

instance_mock = MagicMock(spec_set = BurritoBowl.steak_special())
print(instance_mock.protein)
print(instance_mock.rice)
print(instance_mock.guacamole_portion)
print(instance_mock.add_guac())
# print(instance_mock.add_cheese())
# instance_mock.delicious = True
# print(instance_mock.delicious) 
