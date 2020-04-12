class Student:
    print ("Starting class student")
    # name ="A"
    # grade ="A"
    # rollnum = 23

    def __init__(self, name,grade,rollnum):
        self.name= name
        self.grade= grade
        self.rollnum= rollnum

    def studentinfo(self):
        print ("Name : ", self.name)
        print ("grade : ", self.grade)
        print ("Roll number : ", self.rollnum)

student1 = Student("Anjali", "A",45)
student1.studentinfo()

student2 = Student("Vijay", "F",68)
student2.studentinfo()
