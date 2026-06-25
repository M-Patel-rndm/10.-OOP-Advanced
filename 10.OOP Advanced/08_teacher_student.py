class Teacher:

    def teach(self):
        print("Teacher teaches")


class Student(Teacher):

    def study(self):
        print("Student studies")


obj = Student()

obj.teach()
obj.study()