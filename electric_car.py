from car import Car


class ElectricCar(Car):
    def __init__(self, brand, model, year, mileage, fuel, c_type, available, transmission, c_id, battery_range):
        super().__init__(brand, model, year, mileage, fuel, c_type, available, transmission, c_id)

        self.battery_range = battery_range

    def __str__(self):
        return f'Car:Electric car and range up to {self.battery_range}\n {self.brand} {self.model} {self.year} {self.car_type}\nFuel type: {self.fuel}\nCurrent mileage: {self.mileage} km\n{"Available" if self.available else "Not available now, check others"}'

