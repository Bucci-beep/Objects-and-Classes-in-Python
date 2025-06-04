class Patient:

    # standard consultation fee
    consultation_fee = 1000

    # initializing instance variables
    def __init__(self, name, age, treatment_cost):
        self.name = name
        self.age = age
        self.treatment_cost = treatment_cost

    # add a total bill method (treatment_cost + consultation_fee)
    def total_bill(self):
        total = self.treatment_cost + Patient.consultation_fee
        return total

# create patients and test the data
patient1 = Patient('Big Meeks', 34, 3500)
patient2 = Patient('Paul Scholes', 42, 5500)
patient3 = Patient('Jamie Button', 56, 3000)

print("====== Patient Bills ======")
print(f"Name: {patient1.name}, Age: {patient1.age}, Total Bill: Kshs {patient1.total_bill()}")
print(f"Name: {patient2.name}, Age: {patient2.age}, Total Bill: Kshs {patient2.total_bill()}")
print(f"Name: {patient3.name}, Age: {patient3.age}, Total Bill: Kshs {patient3.total_bill()}")
