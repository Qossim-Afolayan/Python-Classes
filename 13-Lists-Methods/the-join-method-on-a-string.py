address = ["5000 fifth Avenue", "New York", "NY", "10036"]

print(",".join(address))
print(", ".join(address))
print("".join(address))

print("-".join(["555", "123", "4567"]))
print("!".join(["555", "123", "4567"]))
print("***".join(["555", "123", "4567"]))

def encrypt_message(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for letter in string:
        encrypted_letter_index_position = (alphabet.index(letter) + 2) % 26
        encrypted += alphabet[encrypted_letter_index_position]
        
    return encrypted

print(encrypt_message("abc"))
print()
