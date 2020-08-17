release_dates = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}

# year = release_dates.pop("Java")
# print(year)
# print(release_dates)

release_dates.pop("Go")
print(release_dates)

if "Rust" in release_dates:
    release_dates.pop("Rust")


new_year = release_dates.pop("Ruby", 2000)
print(new_year)

del release_dates["Java"]
print(release_dates)


#del release_dates["Rust"]
# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings. 
# For each string in the list, if the string exists as a dictionary key, 
# delete the key-value pair from the dictionary. 
#
# If the string does not exist as a dictionary key, avoid an error. 
# The return value should be the modified dictionary object.
#
# EXAMPLE:
# my_dict = {
#   "A": 1,
#   "B": 2,
#   "C": 3
# }
#
# strings = ["A", "C"]
# delete_keys(my_dict, strings) => {'B': 2}
def delete_keys(dict, strings):

  for string in strings:
    if string in dict:
      del dict[string]

  return dict 
my_dict = {
  "A": 1,
  "B": 2,
  "C": 3
}

strings = ["A", "C"]
print(delete_keys(my_dict, strings))



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)
