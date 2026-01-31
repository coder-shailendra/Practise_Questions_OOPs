class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name 
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("name:",self.name)
        print("roll_no:",self.roll_no)
        print("marks:",self.marks)
    
    def grade(self):
        if self.marks >= 75:
            g = "A"
        elif self.marks >= 60:
            g = "B"
        elif self.marks >= 40:
            g = "C"
        else:
            g = "F"

        print("grade:",g)    

name = input("Enter name: ")
roll = int(input("Enter roll no: "))
marks = int(input("Enter marks: "))

s = Student(name, roll, marks)
s.display()
s.grade()