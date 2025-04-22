class Doctor:
    """
    Attributes = name, specialty, shift, availability
    Methods = assign_shift(), change_availability(), info()
    Operations = manage availability, status and schedules
    """
    # Step 1 - Initialize
    def __init__(self, name, specialty, shift, availability):
        self.name = name # the doctors name
        self.specialty = specialty # e.g. "Cardiology"
        self.shift = None # no shift has been assigned yet
        self.available = False # starts out as not available

    """
    Step 2 - Give the doctor a shift and mark them as available
    """
    def assign_shift(self, shift):
        if not self.available:
            self.shift = shift # record the new shift
            self.available = True # now they are available
            print(f"{self.name} is available is assigned to the {self.shift} shift.")
        else:
            print(f"{self.name} is already on the {self.shift} shift therefore he is unavailable.")

    """
    Step 3 - Change a doctor's availability
    """
    def change_availability(self, available):
        if available and not self.shift: # means the doctor is available and not assigned to a shift
            print(f"⚠ {self.name} has no shift assigned; cannot become available.")
            return
        # otherwise, accept the change, this makes the doctor available
        self.available = available

        status = "available" if available else "unavailable"

        print(f"{self.name} is currently {status}")

    def info(self):
        print("----- Doctor Information -----")
        print(f"Name:   {self.name}")
        print(f"Specialty: {self.specialty}")
        print(f"Shift: {self.shift if self.shift else '(none)'}")
        print(f"Available {'Yes' if self.available else 'No'}")
        print("-------------------------------")

dr = Doctor("Alice", "Pediatrics", "Evening", False)
dr.info()
dr.assign_shift("Morning")
dr.change_availability(True)
dr.info()








