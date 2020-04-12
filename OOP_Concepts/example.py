print("outside class Dog")

class Dog:

    def run(self):
        print("The dog is running...")

    def __init__(self, name, color):
        print("Inside parameterized constructor")
        self.name = name
        self.color = color

    print("inside class Dog")
    name = "Max"
    color = "brown"


newDog = Dog("Puppy", "white")
print("parameterized object")
print("Name: " +newDog.name + "  Color: "+ newDog.color)
newDog.run()

# myDog = Dog()
# print("Name: " +myDog.name + "  Color: "+ myDog.color)
# myDog.run()
#
# dogA = Dog()
# print("Name: " +dogA.name + "  Color: "+ dogA.color)
# dogA.run()

