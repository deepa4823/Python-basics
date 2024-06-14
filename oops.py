#CLASS ,OBJECTS, CONSTRUCTOR, SELF
class student:
    def __init__(self, a,b):
        self.a1=a
        self.b1=b
    def classes(self):
        print("the classes are boring")
        self.s="boring"
    def assignments(self):
        print("assignments are more")
        self.assign="more"
        pro=c*d
        print(pro)
    def problem(self):
        print("the problem is classes and assignments")
        c_s=self.s-10
        print(c_s,self.assign)
        print(self.a1+self.b1)
day_2=student(20,30)
print("from below im making function calls")
day_2.classes()
day_2.assignments(2,10)
day_2.details()
