class car:

    def __init__(self):
        print("Instance of class car created")

    def start(self):
        print("Starting the car....")

    def stop(self):
        print("Stopping the car....")

class superCar():

    def __init__(self):
        print("Instance of superCar created")

    def start(self):
        print("Starting the super car.... 0 to 100 in 2.5 sec")

    def convertible(self):
        print("The car has convertible feature")

class BMW(car, superCar):
    pass

b = BMW()
b.start()



