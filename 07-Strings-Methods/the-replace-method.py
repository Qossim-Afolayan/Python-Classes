phone_number = "555 555 1234"

#to replace all spaces with a dash (to swap)
print(phone_number.replace(" ", "-"))
print(phone_number.replace('5', '9'))
 #strings are immutable
print(phone_number)

def fancy_cleanup(str):
    return str.strip().replace("g", "z").replace(" ", "!")

print(fancy_cleanup("       geronimo crikey      "))
print(fancy_cleanup("grade"))

