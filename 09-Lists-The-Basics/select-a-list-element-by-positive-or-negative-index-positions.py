print("organic"[5])


web_browser = ["Chrome", "Firefox", "Safari", "Opera", "Edge"]

print(web_browser[1])
print(web_browser[2])
print(web_browser[3])
print(web_browser[4])

print(web_browser[2][4])

presidents = ["Washington", "Adams", "Jefferson"]

print(presidents[-1])

def first_and_last(list):
    return list[0] + list[-1]
    
    
print(first_and_last(["a", "b", "c"]))


def product_of_even_indices(numbers):
    if len(numbers) == 6:
        return numbers[0] * numbers[2] * numbers[4]

print(product_of_even_indices([1, 2, 3, 4, 5, 6]))

def first_letter_of_last_string(strings):
    return strings[-1][0]
    
print(first_letter_of_last_string(["cat", "dog", "zebra"]))



