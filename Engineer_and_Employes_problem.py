class employes:
    def __init__(self, role, dept ,salary):
        self.role = role
        self.dept = dept 
        self.salary = salary

    def showdetail(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)


class engineer(employes):
    def __init__(self,name,age,):
        self.name = name 
        self.age = age
        super().__init__("engineer","IT","75,000")

engg1 = engineer("elon musk","40")
engg1.showdetail()        