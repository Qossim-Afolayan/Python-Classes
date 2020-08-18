stats = {
    "name": "BBQ Chicken",
    "price": 19.99,
    "size": "Extra Large",
    "ingredient": ["Chicken", "Onions", "BBQ Sauce"]
}

class Pizza():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)

bbq = Pizza(stats)

stats_to_delete = ["size", "diameter", "spiciness", "ingredient"]

print(bbq.size)

for stat in stats_to_delete:
    if hasattr(bbq, stat):
        delattr(bbq, stat)

# print(bbq.size)
# print(bbq.ingredient)



