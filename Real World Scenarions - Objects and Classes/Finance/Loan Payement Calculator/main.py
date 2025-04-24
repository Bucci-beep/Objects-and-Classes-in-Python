from loan_payment import Loan

def main():
    test_loans = [
        (200_000, 0.045, 30),
        (150_000, 0.036, 15),
        (25_000, 0.055, 5),
        (10_000, 0.075, 3),
        (50_000, 0.0,   10),
    ]

    for principal, rate, term in test_loans:
        loan = Loan(principal, rate, term)
        loan.info()
        print()

if __name__ == "__main__":
    main()
