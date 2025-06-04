class SoftwareProduct:

    support_fee = 500 # fixed fee added to all products, appears as a class_variable

    # instantiating the instance variables
    def __init__(self, name, base_price, discount_rate):
        self.name = name
        self.base_price = base_price
        self.discount_rate = discount_rate

    def final_price(self): # calculates the final price by applying product specific discount to the base price and then adding the support fee
        # apply discount to the base price
        discounted_price = self.base_price * (1- self.discount_rate)
        total_price = discounted_price + SoftwareProduct.support_fee
        return total_price

product1 = SoftwareProduct('ProductivitySuite', 5000, 0.25)
product2 = SoftwareProduct('SecurityShield', 5000, 0.1)

# printing the final price
print(product1.final_price())
print(product2.final_price())