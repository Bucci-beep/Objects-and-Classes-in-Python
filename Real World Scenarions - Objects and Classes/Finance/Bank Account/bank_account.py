class BankAccount:

    # class variable
    minimum_balance = 1000

    # initialize instance variables
    def __init__(self, account_holder, account_balance, interest_rate):
        self.account_holder = account_holder
        self.account_balance = account_balance
        self.interest_rate = interest_rate

    # a method that applies interest(calculates interest rate and adds it to the balance on the account balance)
    def apply_interest(self):
       self.account_balance += self.interest_rate * self.account_balance
       return self.account_balance

    # method to check if the balance is above o below the minimum balance
    def check_minimum_balance(self):
        if self.account_balance >= BankAccount.minimum_balance:
            return ("Account is in good standing.")
        else:
            return ("Account below minimum balance! Action required.")

acc1 = BankAccount('Alice', 50000, 0.03)
acc2 = BankAccount('Iante', 70000, 0.08)

print("====== Bank Account Details ======")

# Alice Bank Account
print(f"Name: {acc1.account_holder}")
print(f"Initial Balance: ${acc1.account_balance:,.2f}")
acc1.apply_interest()
print(f"Balance After Applying Interest: ${acc1.account_balance:,.2f}")
print(f"Minimum Balance Status: {acc1.check_minimum_balance()}")
print()

# For Iante
print(f"Name: {acc2.account_holder}")
print(f"Initial Balance: ${acc2.account_balance:,.2f}")
acc2.apply_interest()
print(f"Balance After Applying Interest: ${acc2.account_balance:,.2f}")
print(f"Minimum Balance Status: {acc2.check_minimum_balance()}")

