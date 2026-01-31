class Result:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name)
        print(self.marks)

    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")


name = input("Enter name: ")
marks = int(input("Enter marks: "))

r = Result(name, marks)
r.display()
r.result()
