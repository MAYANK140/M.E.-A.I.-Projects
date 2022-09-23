class Student:
    def __init__(self, name, roll, marks):
        self.n = name
        self.r = roll
        self.m = marks
    def display(self):
        print('Student Name : ', self.n)
        print('Student Roll : ', self.r)
        print('Student Marks : ', self.m)
S1 = Student ('Alex', 101, 78.25)
S2 = Student ('Bob', 102, 62.55)
S1.display()
S2.display()