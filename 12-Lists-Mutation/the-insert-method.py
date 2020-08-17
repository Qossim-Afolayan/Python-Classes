plays = ["Hamlet", "Macbeth", "King Lear"]

plays.insert(1, "Julius Caesar")
print(plays)

plays.insert(0, "Romeo & Juliet")
print(plays)

plays.insert(10, "A Midsummer Night's Dream")
print(plays)

def long_strings(strings):
    longs = []
    for string in strings:
        if len(string) < 5:
            continue
        else:
            longs.append(string)
            
    return longs

print(long_strings(["Ace", "Cat", "Job"]))
print(long_strings(["Hello", "Goodbye", "Sam"]))

def only_evens(numbers):
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            continue
        
    return even

print(only_evens([4, 8, 15, 16, 23, 42]))