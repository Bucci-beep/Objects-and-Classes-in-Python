class BudgetCategory:
    def __init__(self, category_name, limit):
        self.category_name = category_name
        self.limit = limit
        self.expenses = []

    def add_expense(self, amount):
        if amount < 0:
            print(f"⚠️  Expense amount must be positive.")
            return
        self.expenses.append(amount)
        print(f"➕ Added an expense of {amount:.2f} to '{self.category_name}'.")

    def remaining_budget(self):
        """Should bring about the budget left."""
        total_spent = sum(self.expenses) #Calculate what has been spent so far
        return self.limit - total_spent #Returns what's left from the set limit after adding up all expenses

    def info(self):

        total_spent = sum(self.expenses)
        remaining = self.remaining_budget()

        print("----- Budget Category Info -----")
        print(f"Category Name: {self.category_name}")
        print(f"Budget Limit: {self.limit:.2f}")
        print(f"Total Expenses: {total_spent:.2f}")
        print(f"Remaining Budget: {remaining:.2f}")
        print(f"----------------------------------")


groceries = BudgetCategory("Groceries", 300.00)
groceries.info()

groceries.add_expense(45.50)
groceries.add_expense(10.00)
groceries.info()

groceries.add_expense(-5)

print("Remaining:", groceries.remaining_budget())

