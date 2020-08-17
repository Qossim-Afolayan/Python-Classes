#A set is a mutable, unordered data structure that prohibits duplicated values
# Set contains only immutable values
stocks = { "MSFT", "FB", "IBM", "FB" }
print(stocks)

prices = { 1, 2, 3, 4, 5, 3, 2, 1 }
print(prices)

reg_num = { (1, 2, 3), (4, 5, 2), (1, 2, 3) }
print(reg_num)

print(len(stocks))
print(len(prices))
print(len(reg_num))

print("MSFT" in stocks)
print("GOOG" not in stocks)

for number in prices:
    print(number)

for numbers in reg_num:
    for num in numbers:
        print(num)

squares = { number ** 2 for number in [-5, -4, -3, 3, 4, 5] }
print(squares)
print(len(squares))
