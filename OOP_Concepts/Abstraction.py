from abc import ABC, abstractmethod

class RBI(ABC):
    @abstractmethod
    def getROI(self):
        pass

    def getName(self):
        print ("Parent Class")
        return "Parent Bank"

class SBI(RBI):
    @abstractmethod
    def getROI(self):
        # pass
        print("ROI: 8")
        return 8

    def getName(self):
        print ("Bank name: SBI")

class HDFC(RBI):
    def getROI(self):
        print("ROI: 9")
        return 9

    def getName(self):
        print ("Bank name: HDFC")

# r = RBI()
s = SBI()
s.getROI()
s.getName()
h = HDFC()
h.getROI()
h.getName()
