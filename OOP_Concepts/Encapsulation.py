class Employee:
    def __init__(self):
        self.__age = 50

    def getAge(self):
        return self.__age

    def setAge(self, newAgeValue):
        self.__age = newAgeValue

    def __vote(self, age):
        if int(age)<18:
            print("Not permitted to vote")
        else:
            print("Permitted to vote")

emp = Employee()
print(emp.__age)
emp.__age = 10
print(emp.__age)

print(emp.getAge())
print(emp._Employee__age)
# Employee.__vote(emp.getAge())
emp.setAge(10)
print(emp.getAge())
# Employee.__vote(emp.getAge())
