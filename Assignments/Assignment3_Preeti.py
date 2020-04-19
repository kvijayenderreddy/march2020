class Car:
    def start(self):
        print("Start the car")

    def stop(self):
        print("Stop the car")


class SportsCar:
    def aerodynamics(self):
        print("Aerodynamic")

    def topSpeedInfo(self):
        print("Topspeedinfo")


class BMW(Car, SportsCar):
    def parkingAssistance(self):
        print("BMW Car")

# C1 = Car()
# C1.start()
# C1.stop()
#
# C2 = SportsCar()
# C2.aerodynamics()
# C2.topSpeedInfo()
#
# C3 = BMW()
# C3.start()
# C3.stop()
# C3.aerodynamics()
# C3.topSpeedInfo()
# C3.parkingAssistance()
# ================================================

class Calculator:

    def __init__(self):
        print("creating the instance of class Calculator")

    def add(self, a, b):
        return ("Add:", (a+b))

    def subtract(self, a, b):
        return ("Sub", (a-b))

    def multiplication(self, a, b):
        return ("Multiply:", (a*b))

    def division(self, a, b):
        return ("Division:", (a/b))


class Area:

    def __init__(self):
        print("creating the instance of class Area")

    def rectangleArea(self, l, b):
        print("RectangleArea:", (l*b))

    def squareArea(self, l):
        print("SquareArea:", (l*l))


class Multipurpose(Calculator, Area):

    def __init__(self):
        print("creating the instance of class Multipurpose")

    # print("Multipurpose class")

C1 = Calculator()
C1.add(10, 20)
C1.subtract(20, 10)
C1.multiplication(3, 5)
C1.division(20, 5)

A1 = Area()
A1.rectangleArea(3, 2)
A1.squareArea(5)

M1 = Multipurpose()
M1.add(2, 3)
M1.subtract(5, 4)
M1.multiplication(2, 2)
M1.division(10, 2)
M1.rectangleArea(2, 2)
M1.squareArea(7)
