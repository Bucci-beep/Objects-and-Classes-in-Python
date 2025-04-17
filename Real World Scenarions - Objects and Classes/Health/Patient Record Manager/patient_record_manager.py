class Patient:
    def __init__(self,name, age, gender, condition, room_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        self.room_number = room_number
        self.admitted = False

    def admit(self):
        if not self.admitted:
            self.admitted = True
            print(f"{self.name} has been admitted to room {self.room_number}.")
        else:
            print(f"{self.name} is already admitted.")

    def discharge(self):
        if self.admitted:
            self.admitted = False
            print(f"{self.name} has been discharged.")
        else:
            print(f"{self.name} is not currently admitted.")

    def update_condition(self, new_condition):
        old_condition = self.condition
        self.condition = new_condition
        print(f"{self.name}'s condition updated from {old_condition} to {new_condition}.")

    def info(self):
        print("----- Patient Information -----")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Condition: {self.condition}")
        print(f"Room Number: {self.room_number}")
        print(f"Admitted: {'Yes' if self.admitted else 'No'}")
        print("------------------------------")

patient1 = Patient("Alice", 30, "Female", "Flu", 101)
patient1.admit()            # Will admit and print admission message
patient1.info()             # Will display patient details
patient1.update_condition("Recovering")  # Update her condition
patient1.discharge()        # Will discharge and print message
patient1.info()             # Will show updated info with 'Admitted: No'
