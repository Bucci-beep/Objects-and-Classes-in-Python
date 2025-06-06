from psutil import disk_io_counters


class Book:

    # class variable
    discount = float(0.0)

    #insance variables
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # instance method
    def apply_discount(self):
       self.price = self.price * (1 - Book.discount)

    # class method
    @classmethod
    def set_discount(cls, amount):
        cls.discount = amount

    # static method
    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and len(title.strip())  > 0

book1 = Book('Nearly all men in Lagos are mad', 'Damilare Kuku', 400)
book2 = Book('The River and the Source', 'Margaret Ogolla', 1200)

# set a 10% discount
Book.set_discount(0.10)

# print prices before discount
print(f"Book 1 price before discount: Kshs {book1.price}")
print(f"Book 2 price before discount: Kshs {book2.price}")

#apply discount
book1.apply_discount()
book2.apply_discount()

# print prices after discount
print(f"Book 1 price after discount: Kshs {book1.price}")
print(f"Book 2 price after discount: Kshs {book2.price}")

# test static method
print(Book.is_valid_title("Advanced Python"))  # True
print(Book.is_valid_title(""))                # False