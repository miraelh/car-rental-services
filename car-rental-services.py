

class Vehicle:
    def __init__ (self, brand, model, year, rental_price_per_day):
        self.brand = brand    
        self.model = model
        self.year = year
        self._rental_price_per_day = rental_price_per_day
    
    def display_info(self):
        print(f"{self}: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self._rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        total_rental_cost = self._rental_price_per_day*days
        return total_rental_cost




class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        self.seating_capacity = seating_capacity
        super().__init__(brand, model, year, rental_price_per_day)