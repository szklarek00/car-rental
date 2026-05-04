from time import sleep
from car import Car
from customer import Customer
from electric_car import ElectricCar
from rental import Rental
from rental_office import RentalOffice

car1 = Car('Toyota', 'Corolla', 2021,120000, 'hybrid', 'sedan', True, 'automatic', 1)
car2 = Car('Toyota', 'Corolla', 2019,180000, 'hybrid', 'kombi', True, 'automatic', 2)
car3 = Car('BMW', 'Serie 5', 2022,64000, 'diesel', 'sedan', True, 'automatic', 3)
car4 = ElectricCar('Tesla', 'Uknown', 2022, 12342, 'electric', 'sedan', True, 'automatic', 4, 800)

customer1 = Customer('Jan Kowalski', 'CAD131323')
customer2 = Customer('Krzysztof Nowak', 'KER79065')

office = RentalOffice()
office.add_car(car1)
office.add_car(car2)
office.add_car(car3)
office.add_car(car4)
sleep(2)
office.rent_car(customer1, car2)
office.rent_car(customer2, car3)
sleep(2)
office.return_rental_cars(customer1, car2)
office.rental_history()

