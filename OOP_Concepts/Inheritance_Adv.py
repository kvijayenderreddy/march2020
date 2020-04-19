# method Overloading
# Method Overriding
# MultipleInheritance - same method names

class Car:
    def start(self):
        print("Start the Car")

    def stop(self):
        print("Stop the car")

class SportsCar:

    def start(self):
        print("Start the Sports Car")

    def aerodynamics(self):
        print("Aerodynamic")

    def topSpeedInfo(self):
        print("Topspeedinfo")

class BMW(SportsCar, Car):

    # def start(self):
    #     print("speed of 200 KMPH in 0 to 3 sec")

    def parkingAssistance(self):
        print("BMW Car")

C1 = Car()
C1.start()
# C1.start("150 KMPH")
C1.stop()

C2 = SportsCar()
C2.aerodynamics()
C2.topSpeedInfo()

C3 = BMW()
C3.start()
C3.stop()
C3.aerodynamics()
C3.topSpeedInfo()
C3.parkingAssistance()
# ================================================
'''
# LivingThings
-Move
-Move
# Animals
-Move
# Birds
-Move
# Lion (LivingThings, animals)

# Eagle (LivingThings, birds)

'''
