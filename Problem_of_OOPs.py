class Car:
    colour = "black"
def start():
    print("car started..")

def stop():
    print("car stoped..")

class ToyotaCar(Car): 
    def __init__(self,name):
        self.name = name 

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")
print(car1.colour)
print(car2.name)
print(car1.name)
