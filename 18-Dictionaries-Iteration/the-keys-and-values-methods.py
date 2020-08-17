Books_prices = {
    "Sahih Bukhari": 4000,
    "Sahihu Muslim": 3000,
    "Riyadh Salihee": 1000
}

print(Books_prices.keys())
print(type(Books_prices.values()))

print(type(Books_prices.keys()))
print(Books_prices.values())

for book in Books_prices.keys():
    print(f"The next book is {book}")


for price in Books_prices.values():
    print(f"The next price is {price}")

print("Sahih Bukhari" in Books_prices.keys())
print("Nawaawi" in Books_prices.keys())

print(4000 in Books_prices.values())

print(len(Books_prices))
print(len(Books_prices.values()))
print(len(Books_prices.keys()))

def common_elements(dictionary):
    # list = []
    # for key in dictionary:
    #     if key in dictionary.values():
    #         list.append(key)
            
    return [key for key in dictionary.keys() if key in dictionary.values()]

my_dict = {
  "A": "K",
  "B": "D",
  "C": "A",
  "D": "Z"
}

print(common_elements(my_dict))