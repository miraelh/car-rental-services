

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
    

    def get_rental_price_per_day(self):
       return self._rental_price_per_day
        
    def set_rental_price_per_day(self, rental_price_per_day):
        self._rental_price_per_day = rental_price_per_day



class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        self.seating_capacity = seating_capacity
        super().__init__(brand, model, year, rental_price_per_day)

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self._rental_price_per_day}/day")


class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_capacity, rental_price_per_day):
        self.engine_capacity = engine_capacity
        super().__init__(brand, model, year, rental_price_per_day)
    
    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine capacity: {self.engine_capacity}, Rental Price: ${self._rental_price_per_day}/day")


def show_vehicle_info(vehicle):
    vehicle.display_info()  


car1 = Car("Toyota","Corolla", "2020", 50, 5)
car2= Car("Nissan", "X-Trail", 2019, 70, 7)

bike1= Bike("Yamaha", "R1", 2019, "998cc", 30)
bike2= Bike("Vespa", "Primavera", 2024, "155cc", 20)


print(show_vehicle_info(car1))
print(show_vehicle_info(car2))
print(show_vehicle_info(bike1))
print(show_vehicle_info(bike2))
