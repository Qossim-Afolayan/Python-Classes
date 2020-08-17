books = (12, 14, 199)

print(len(books))
print(books[0])
print(books[-3])

print(books[0:3])

addresses = (
    ["Block 42", "Lighthouse", "Estate", "Lagos"],
    ["block 58", "Iponri", "Estate", "Lagos"],
    1,
    3
)


addresses[1][2] = "Street"
print(addresses)

print(dir(books))

print(addresses.index(["Block 42", "Lighthouse", "Estate", "Lagos"]))
print(addresses.count(["block 58", "Iponri", "Street", "Lagos"]))

print(addresses[2])