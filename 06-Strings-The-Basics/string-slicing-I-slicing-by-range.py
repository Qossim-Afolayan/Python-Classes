#String Slicing is the extraction of a subset of a string may be more than a character
#It's based on the index position
#Left offset(inclusive) and Right offset(exclusive)
a = "I actually did write many sentences without the first alphabet"
print(a[0:10])
print(a[0:17])
print(a[19:32])
print(a[10:100])

print(a[34:-6])
print(a[-8:-6])
print(a[-8:-32])

print("\n")

print(a[5:])
print(a[13:])
print(a[-20:])

print("\n")

print(a[:10])
print(a[0:10])
print(a[:23])
print(a[:-3])






print(a[:])