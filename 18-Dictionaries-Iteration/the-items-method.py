college_courses = {
    "History": "Mr Washington",
    "Maths": "Mr Newton",
    "Science": "Mr Einstein"
}

for course, professor in college_courses.items():
    print(f"The course {course} is being taught by {professor}")


for _, professor in college_courses.items():
    print(f"The next professor is {professor}")




def invert(dictionary):
    dict = {}
    for key, value in dictionary.items():
        dict.setdefault(value, key)

    return dict

my_dict = {
  "A": "B", 
  "C": "D",
  "E": "F"
}

print(invert(my_dict))




