print("fast" in "breakfast")
print("fast" in "Dinner")

meals = ["breakfast", "lunch", "dinner"]

print("lunch" in meals)
print("dinner" in meals)
print("Breakfast" in meals)

print()

test_scores = [99.0, 35.0, 23.5]
print(99.0 in test_scores)
print(99 in test_scores)
print(23.5 in test_scores)
print(43.7 in test_scores)

print()

print("lunch" not in meals)
print("breakfast" not in meals)
print(1000 not in test_scores)
print(35 not in test_scores)

if 1000 not in test_scores:
    print("That value is not in there!")

print [1, 2, 3] not in [1, 2, 3]