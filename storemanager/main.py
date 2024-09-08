class Item():

    pay_rate = 0.8 #price after discount is applied

    def __init__(self, name: str, price: float, quantity=0):

        #running validations on recieved arguments
        assert quantity >= 0, f"quantity {quantity} CANNOT be lower than zezo"


        #assign self to object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_net(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Hey", 1000, 2)

item1.apply_discount()

print(item1.price)
