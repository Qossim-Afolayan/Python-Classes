#Sorted method mutates an object while sorted function create a brand new object 
numbers = [4, 2, 9,7]
print(sorted(numbers))
print(numbers)

salaries = {
    "Executive Assistance": 40,
    "CEO": 100
}
print(sorted(salaries))
print(salaries)

wheel_count = {
    "truck": 2,
    "car": 4,
    "bus": 8
}
for vehicle, wheel in sorted(wheel_count.items()):
    print(f"The next vehicle is {vehicle} and it has {wheel} wheels")

    
