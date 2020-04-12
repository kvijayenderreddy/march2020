class Animal:
    def speak(self):
        print("Animal is speaking...")



class Dog(Animal):
    def bark(self):
        print("Dog is barking")

a = Animal()
a.speak()
# a.bark()

d = Dog()
d.speak()
d.bark()
