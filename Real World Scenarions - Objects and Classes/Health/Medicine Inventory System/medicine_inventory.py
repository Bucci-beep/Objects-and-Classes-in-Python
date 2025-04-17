from datetime import datetime

class Medicine:
    """
    Attributes : name, manufacturer, quantity, expiry date
    Methods : restock, dispense, is_expired, info

    """
    #Initialise the constructor
    def __init__(self, name, manufacturer, quantity, expiry_date):
        self.name = name
        self.manufacturer = manufacturer
        self.quantity = quantity
        self.expiry_date = expiry_date

        #Method 1 - restock
    def restock(self,amount):
        self.quantity += amount
        print(f"{self.name} restocked with {amount} units. Total in stock:{self.quantity}")

    def dispense(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            print(f"Dispensed {amount} units of {self.name}. Remaining: {self.quantity}")

    def is_expired(self):
        today = datetime.today().date()
        expiry = datetime.strptime(self.expiry_date, '%Y-%m-%d').date()
        return expiry < today

    def info(self):
        print("----- Medicine Information -----")
        print(f"Name: {self.name}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Quantity in stock: {self.quantity}")
        print(f"Expiry Date: {self.expiry_date}")
        print(f"Expired: {'Yes' if self.is_expired() else 'No'}")
        print("--------------------------------")


panadol = Medicine("Panadol", "GSK", 10, "2025-06-01")

panadol.info()
panadol.dispense(3)
panadol.restock(5)
print("Is expired?", panadol.is_expired())
panadol.info()



