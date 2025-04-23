class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type


    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"✅ {amount} deposited. New balance: {self.balance}")
        else:
            print(f"⚠ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print(f"⚠ Deposit amount must be positive!")
        elif amount > self.balance:
            print(f"❌ Insufficient funds! Current balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"💰 {amount} withdrawn. New balance: {self.balance}")

    def display_balance(self):
        print("----- Bank Account Info -----")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance}")
        print("----------------------------------")

account1 = BankAccount("John Doe", 500, "Savings")
account1.display_balance()
account1.deposit(150)
account1.withdraw(200)
account1.display_balance()
