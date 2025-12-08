from car import Car

class RentalOffice:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print('New car added.')

    def available_cars(self):
        for cars in self.cars:
            if  cars.available == True:
                print(f'Available cars: \n')
                cars.display_info()




office = RentalOffice()
car1 = Car('Toyota', 'Corolla', '2022', 72341, 'hybrid', 'sedan', True, 'automatic', 1)
car2 = Car('BMW', 'Serie 3', '2017', 127531, 'diesel', 'sedan', True, 'automatic', 2)
office.add_car(car1)
office.add_car(car2)
office.available_cars()
