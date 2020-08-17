asaatidha = {
    "Umariyyah": "Abdurrahman Hassan",
    "Naseeha": "Dawahman",
    "Madinah": "Abu Taymiyya"
}

print(asaatidha.get("Madinah"))
print(asaatidha.get("Green lane", 'Abu Usaamah'))
print(asaatidha)

# asaatidha.setdefault("Green lane")
# print(asaatidha)

asaatidha.setdefault("Green lane", "Abu Usaamah")
print(asaatidha)

asaatidha.setdefault("Green lane", "Abu Ibrahim")
print(asaatidha)

# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#
# EXAMPLE:
# detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}

def to_dictionary(lists):
    dictionary = {}
    for list in lists:
        dictionary[list] = lists.index(list)

    return dictionary


print(to_dictionary(["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]))

# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 
# 2 strings with 7 letters, and 1 string with 4 letters.
# def length_counts(strings):
#     diction = {}
#     for string in strings:
#         if len(string) in diction:
#             diction[len(string)] += 1

#         else:
#             diction[len(string)] = 1

#     return diction
#print(length_counts(["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]))
def length_counts(elements):
    result = {}
    for element in elements:
        length = len(element)
        current_count = result.get(length, 0)
        counts = current_count + 1
        result[length] = counts

    return result
print(length_counts(["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]))
mystery = {

  "a": 2

}



mystery.setdefault("A", 5)

mystery.setdefault("a", 10)

mystery.setdefault("B", 30)

mystery.setdefault("B", 40)

print(mystery)