class Student():
    def __init__(self, maths, history, writing):
        self.maths = maths
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.maths + self.history + self.writing

    def __eq__(self, other_student):
        return self.grades == other_student.grades


bob = Student(maths = 90, history = 90, writing = 90)
moe = Student(maths = 100, history = 80, writing = 90)
joe = Student(maths = 45, history = 50, writing = 40)


print(bob.grades)
print(bob == moe)
print(joe == bob)

print(bob != moe)
print(bob != joe)
