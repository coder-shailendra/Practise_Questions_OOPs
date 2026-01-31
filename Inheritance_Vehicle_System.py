class vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print("brand:",self.brand)
        print("speed:",self.speed)

class Car(vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def show(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)
        print("Fuel Type:", self.fuel_type)



c1 = Car("Toyota", 120, "Petrol")
c1.show()