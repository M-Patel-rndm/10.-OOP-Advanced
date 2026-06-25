class Vehicle:

    def display(self):
        print("This is a Vehicle")


class Car(Vehicle):

    def display_car(self):
        print("This is a Car")


class ElectricCar(Car):

    def display_electric(self):
        print("This is an Electric Car")


car = ElectricCar()

car.display()
car.display_car()
car.display_electric()