class Employee:

    def __init__(self, name, sal):
        self._name = name
        self._sal = sal

emp = Employee("captain", 10000)
print("salary:", emp._sal)

class HR(Employee):
    def task(self):
        print("We manage Employee recruitment")

hrEmp = HR("newCaptain", 500000)
print(hrEmp._sal)
hrEmp.task()

class HelpDesk:
    print("HelpDesk Dept")

# hd = HelpDesk()
# print(hd._sal)

'''
Create a class "Student" with below properties:
   name, grade, rollNumber

    then create two objects of the Student class with different property values to it
    create method as studentInfo()
'''