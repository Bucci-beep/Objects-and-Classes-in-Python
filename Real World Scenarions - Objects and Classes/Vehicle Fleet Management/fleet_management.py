class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def vehicle_info(self):
        print(f"{self.make} {self.model} {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def load_cargo(self, weight):
        if weight <= self.payload_capacity:
            print(f"Loaded {weight} kg of cargo successfully!")
        else:
            print(f"Cannot load {weight} kg. it exceeds capacity of {self.payload_capacity}")


car_1 = Car('Toyota', 'Camry', 2025, 4)
truck_1 = Truck('Ford', 'E-150', 2019, 1000)

car_1.vehicle_info()
truck_1.vehicle_info()

truck_1.load_cargo(800)
truck_1.load_cargo(1220)
