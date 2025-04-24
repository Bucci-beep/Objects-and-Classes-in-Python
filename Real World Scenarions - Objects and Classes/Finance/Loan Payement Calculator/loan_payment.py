class Loan:
    def __init__(self, principal, interest_rate, term_years):
        if principal <= 0: #You must borrow something
            raise ValueError("Principal must be positive!")
        if interest_rate < 0:
            raise ValueError("Interest rate must be positive!")
        if term_years <= 0: #Zero-year terms break the formula(divide by zero)
            raise ValueError("Term must be at least 1 year!")

        self.principal = principal
        self.interest_rate = interest_rate
        self.term_years = term_years

    def calculate_monthly_payment(self):
        r = self.interest_rate / 12
        n = self.term_years * 12
        p = self.principal

        #Handle zero interest loans to avoid division by zero
        if r == 0:
            return p / n

        return (p * r) / (1 - (1 + r)** -n)

    def info(self):
        monthly_payment = self.calculate_monthly_payment()

        print("----- Loan Payment Calculator-----")
        print(f"Principal: {self.principal:,.2f}")
        print(f"Interest Rate: {self.interest_rate *100:.3f}% per year")
        print(f"Term Years: {self.term_years} years")
        print(f"Monthly Payment: ${monthly_payment:,.2f}")
        print("-----------------------------------")

