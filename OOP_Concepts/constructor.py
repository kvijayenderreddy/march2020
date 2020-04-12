class Person:
    print("Inside the class")
    # name = "xyz"
    # age = 33
    # gender = "male"

    def __init__(self, name, age, gender):
        print("Inside the constructor")
        self.name = name
        self.age = str(age)
        self.gender = gender

    def introduction(self):
        print("Hello my name is " + self.name)
        print("Hello my age is " + self.age)


p1 = Person("yograj", 30, "male")
p1.introduction()
# print(p1.name)
