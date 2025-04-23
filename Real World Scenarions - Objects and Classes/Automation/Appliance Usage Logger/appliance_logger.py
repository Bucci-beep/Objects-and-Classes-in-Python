class Appliance:
    def __init__(self, name, power_rating = 100):
        self.name = name
        self.power_rating = power_rating
        self.usage_hours = 0 # no usage yet

    def log_usage(self, hours):
        if hours <=0:
            print(f"⚠ {self.name}: Logged hours must be greater than zero!")
            return
        old = self.usage_hours
        self.usage_hours += hours
        print(f"🕒 Logged {hours}h for '{self.name}'. Total: {old}h → {self.usage_hours}h.")

    def reset_usage(self):

        if self.usage_hours == 0:
            print(f"⚠  {self.name}: Usage is already at zero.")
        else:
            self.usage_hours = 0
            print(f"🔄 '{self.name}' usage reset to 0h.")

    def info(self):
        print("----- Usage Logger Information -----")
        print(f"Name: {self.name}")
        print(f"Power Rating: {self.power_rating}W")
        print(f"Usage Hours: {self.usage_hours}h")
        print("--------------------------------------")


machine = Appliance("Ex-machina", power_rating=100)
machine.info()

machine.log_usage(5)
# 🕒 Logged 5h for 'Ex-machina'. Total: 0h → 5h

machine.reset_usage()
# 🔄 'Ex-machina' usage reset to 0h

machine.info()




