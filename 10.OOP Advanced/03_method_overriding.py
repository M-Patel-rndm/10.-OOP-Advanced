class Parent:

    def show(self):
        print("Parent Class Method")


class Child(Parent):

    def show(self):
        print("Child Class Method")


obj = Child()

obj.show()