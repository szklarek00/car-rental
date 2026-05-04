from datetime import datetime

class Rental:
    def __init__(self, customer, car):
        self.customer = customer
        self.car = car
        self.start_date = datetime.now()
        self.end_date = None
        self.amount = 100

    def calculate_cost(self):
        if self.end_date is not None:
            rental_period = (self.end_date - self.start_date).days
            payment = rental_period * self.amount
            return f'Total amount paid: {payment}'
        else:
            return 'Please return the car to calculate payment!'

    def __str__(self):
        return (
            f'Rental: {self.customer.name}\n'
            f'Car: {self.car.brand} {self.car.model}\n'
            f'From: {self.start_date}\n'
            f'To: {"not returned yet" if self.end_date is None else self.end_date}\n'
        )



