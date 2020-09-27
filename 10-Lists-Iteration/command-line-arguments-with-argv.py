import sys

# print(sys.argv)

# print(type(sys.argv)) list

word_length = 2

for arg in sys.argv[1:]:
    word_length += len(arg) #hasken

print(f"The length of all command line arguments is {word_length}")