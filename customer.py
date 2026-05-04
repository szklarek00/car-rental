class Customer:
    def __init__(self, name, driving_license):
        self.name = name
        self.license_number = driving_license
        self.rental_cars = []

    def __str__(self):
        separator = ', '
        results = [str(car) for car in self.rental_cars]
        return f'Client {self.name} \nDriving license number: {self.license_number} \nLast rental cars: {separator.join(results)}'

