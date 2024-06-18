#INHERITANCE

class Faculty: #parent class
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def print_info(self):
        print("faculty information=",self.f_name,self.department,self.f_id)
obj=Faculty("Ashish","computer_science",1001)
obj.print_info()


class cse(Faculty):#child class B
    pass
obj1=cse("Jyothi mam","computer_science",1002)
obj1.print_info()


class ece(Faculty):#child class C
    pass
obj2=ece("Ashok sir","ECE",1003)
obj2.print_info()


class eee(Faculty):#child class D
    pass
obj3=eee("raj sir","eee",1004)
obj3.print_info()


#multiple inheritance
class SubMarks:#class-1
    math=int(input("Enter paper marks of math"))
    DE=int(input("Enter paper marks of design eng"))
    c=int(input("Enter paper marks for c language"))
    english=int(input("Enter paper marks for english"))
#parent class-1
class PractMarks:
    cpract=int(input("Enter practical marks for c languagae"))
class Result:
