class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self, factor):
        return self.num1 * factor

    def divide(self, divisor):
        if divisor == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return self.num1 / divisor

calc = Calculator(10, 5)

print("Add:", calc.add())
print("Subtract:", calc.subtract())
print("Multiply:", calc.multiply(3))
print("Divide:", calc.divide(2))
