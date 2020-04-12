class Animal:
    def speak(self):
        print("Animal is speaking..")


class Dog(Animal):
    def bark(self):
        print("Dog is barking...")

class PuppyDog(Dog):
    def barkSoftly(self):
        print("Puppydog is barking softly...")

a = Animal()
a.speak()

d = Dog()
d.bark()
d.speak()

pd = PuppyDog()
pd.barkSoftly()
pd.bark()
pd.speak()