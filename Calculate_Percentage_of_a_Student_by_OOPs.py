class Student:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths 
    
    @property
    def percentage(self): 
        return str((self.phy + self.chem + self.maths) / 3) + "%"
    
student1 = Student(98,97,96)
print(student1.percentage)

student1.phy = 90
print(student1.percentage)

