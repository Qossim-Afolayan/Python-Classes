employee_salaries = {
    "Guido": 100000,
    "James": 500000,
    "Brandom": 90000
}

extra_employies_salaries = {
    "Yukihiro": 100000,
    "Guido": 3333333
}

employee_salaries.update(extra_employies_salaries)
#extra_employies_salaries.update(employee_salaries)

print(employee_salaries)
print(extra_employies_salaries)


