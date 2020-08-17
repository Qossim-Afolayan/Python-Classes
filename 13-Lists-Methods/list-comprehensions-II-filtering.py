print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"])

print([num / 2 for num in range(21)])

donuts =[
    "Boston Cream",
    "Jelly",
    "Vanilla Cream",
    "Glazed",
    "Chocolate Cream"
]

print([donut for donut in donuts if "Cream" in donut])
print([donut.split(' ')[0] for donut in donuts if "Cream" in donut])

