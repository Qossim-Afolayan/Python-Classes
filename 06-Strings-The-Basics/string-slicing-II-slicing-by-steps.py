#Slicing by steps (intervals)
alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet[0:10:2])
print(alphabet[0:26:3])
print(alphabet[:26:3])
print(alphabet[::3])
print(alphabet[:-1:3])
print(alphabet[0::3])

print("\n")

print(alphabet[4:20:5])
print(alphabet[-20:-8:2])

print(alphabet[::-3])
print(alphabet[::-2])
print(alphabet[::-1])



def last_five_characters(a):
    return a[-5:]

print(last_five_characters("dynasty"))
print(last_five_characters("empire"))


def is_palindrome(b):
    if b[::1] == b[::-1]:
        return True
    else:
        return False
        
print(is_palindrome("racecar"))
print(is_palindrome("yummy"))
        
print("november"[6])

def is_ookay(n):
    if n % 2 == 1:
        return True
    else:
        return False

        number = int(input("please enter an integer: "))
        print(is_okay)