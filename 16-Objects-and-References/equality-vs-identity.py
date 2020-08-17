#Equality tests whether two objects are equal

#Identity checks if two names in a program points to same object (is keyword)

students = ["Bob", "Sally", "Sue"]
athletes = students
nerds = ["Bob", "Sally", "Sue"]

print(students == athletes)
print(students == nerds)

print(students is athletes)
print(students is nerds)

a = 1
b = 1

print(a is b)

a = "hello"
b = "hello"
print(a is b)

web_dev = ["HTML", "CSS", "JavaScript"]

frontend = web_dev



web_dev.append("React")

print(frontend)





