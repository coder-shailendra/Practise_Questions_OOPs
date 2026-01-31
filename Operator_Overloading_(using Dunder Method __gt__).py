class order:
    def __init__(self,items,price):
        self.items = items
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price
    
odr1 = order("chips","20")
odr2 = order("tea","10")
print(odr1>odr2)