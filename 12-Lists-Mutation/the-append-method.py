countries = ["United State", "Canada", "Australia"]
print(countries)
print(len(countries))

countries.append("Japan")
print(countries)
print(len(countries))

countries.append("France")
print(countries)
print(len(countries))

countries.append("Belgium")
print(countries)
print(len(countries))

# for number in range(11):
#     print(number)

def factors(whole):
    result = []
    for number in range(1,whole + 1):
        if whole % number == 0:
            result.append(number)

        
    return result

print(factors(64))
    