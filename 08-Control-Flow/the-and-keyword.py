# def truthy_or_falsy(chk_arg):
#     mn_dt = bool(chk_arg)
#     if mn_dt == True:
#         return "The value of {d} is Truthy".format(d = chk_arg)
#     else:
#         return "The value of {d} is falsy".format(d = chk_arg)

# print(truthy_or_falsy(8))
# print(truthy_or_falsy(""))
# and keyword all conditions must be true 
if 5 < 7 and "rain" == "rain":
    print("Both of these conditions evaluate to true")
if 5 < 7 and "rain" == "fire":
    print("This will not print because at least on of the two condition evaluate to false")
if "rain" == "fire" and 5 < 7:
    print("This will not print because at least on of the two condition evaluate to false")
if "rain" == "fire" and 5 < 3:
    print("This will not print because at least on of the two condition evaluate to false")
#short socket method

value = 95
#if value > 90 and value < 100:
if 90 < value < 100:
    print("This is a shortcut for te win!")

