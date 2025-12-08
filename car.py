class Car:
    def __init__(self, brand, model, year, mileage, fuel, c_type, available, transmission, c_id):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel = fuel
        self.type = c_type
        self.available = available
        self.transmission = transmission
        self.id = c_id


    def display_info(self):
        #print(f'General info about cars:')
        print(f'Car: {self.brand} {self.model} {self.year} {self.type}\nfuel type: {self.fuel}\ncurrent mileage: {self.mileage} km')
        if self.available == True:
            print('Available now!')
        else:
            print('Not available, check others')
        

