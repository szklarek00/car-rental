

class Car:
    def __init__(self, brand, model, year, mileage, fuel, c_type, available, transmission, c_id):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel = fuel
        self.car_type = c_type
        self.available = available
        self.transmission = transmission
        self.car_id = c_id

    def __str__(self):
        return f'Car: {self.brand} {self.model} {self.year} {self.car_type}\nFuel type: {self.fuel}\nCurrent mileage: {self.mileage} km\n{"Available" if self.available else "Not available now, check others"}'

