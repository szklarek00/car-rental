from datetime import datetime
from rental import Rental

class RentalOffice:
    def __init__(self):
        self.cars = []
        self.rentals = []

    def add_car(self, car):
        self.cars.append(car)
        print('New car added.')

    def available_cars(self):
        print('Available cars: \n')
        for car in self.cars:
            if  car.available:
                print(car)

    def rent_car(self, customer, car):
        if car.available:
            rental = Rental(customer, car)
            car.available = False
            self.rentals.append(rental)
            customer.rental_cars.append(rental)
            print('Rental car rented! ')
        else:
            print('No available rental cars. Choose others.')

    def return_rental_cars(self, customer, car):
        for rental in customer.rental_cars:
            if rental.car == car:
                rental.end_date = datetime.now()
                car.available = True
                print('Returned rental car! ')

    def rental_history(self):
        print('Rental history: \n')
        for rental in self.rentals:
            print(rental)

