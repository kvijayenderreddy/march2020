class Calculation1:
    def summation(self, a, b):
        print("sum of the two numbers: ",a,b, (a+b))

class Calculation2:
    def multiplication(self, a, b):
        print("product of the two numbers: ",a,b, (a*b))

class MultiCalculation(Calculation2, Calculation1):
    def division(self, a, b):
        print("Division of two numbers: ",a,b, (a/b))

c1 = Calculation1()
c1.summation(2,3)

c2 = Calculation2()
c2.multiplication(10,20)

mCal = MultiCalculation()
mCal.division(40, 10)
mCal.multiplication(20, 10)
mCal.summation(50, 100)