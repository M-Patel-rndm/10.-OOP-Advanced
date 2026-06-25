class Circle:

    def area(self):
        print("Area of Circle")


class Rectangle:

    def area(self):
        print("Area of Rectangle")


def display_area(shape):
    shape.area()


c = Circle()
r = Rectangle()

display_area(c)
display_area(r)