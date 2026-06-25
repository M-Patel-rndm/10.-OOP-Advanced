class Student:

    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


student = Student()

student.set_marks(85)

print("Marks =", student.get_marks())