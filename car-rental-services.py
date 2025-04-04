

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



print()
print()
show_vehicle_info(car1)
show_vehicle_info(car2)
show_vehicle_info(bike1)
show_vehicle_info(bike2)
print()
print()


# if we are to set the number of days ourselves:

print(f"Rental cost for {car1.brand} {car1.model} for 3 days: ${car1.calculate_rental_cost(3)}")
print(f"Rental cost for {car2.brand} {car2.model} for 3 days: ${car2.calculate_rental_cost(3)}")
print(f"Rental cost for {bike1.brand} {bike1.model} for 5 days: ${bike1.calculate_rental_cost(5)}")
print(f"Rental cost for {bike2.brand} {bike2.model} for 5 days: ${bike2.calculate_rental_cost(5)}")
print()
print()

# if we are to ask the user to give the number of days:
days = int(input("Please enter the number of days you need the vehicle for: "))

print(f"Rental cost for {car1.brand} {car1.model} for {days} days: ${car1.calculate_rental_cost(days)}")
print(f"Rental cost for {car2.brand} {car2.model} for {days} days: ${car2.calculate_rental_cost(days)}")
print(f"Rental cost for {bike1.brand} {bike1.model} for {days} days: ${bike1.calculate_rental_cost(days)}")
print(f"Rental cost for {bike2.brand} {bike2.model} for {days} days: ${bike2.calculate_rental_cost(days)}")
print()
print()

car1.set_rental_price_per_day(55)
print(f"Updated rental price for {car1.brand} {car1.model}: ${car1.get_rental_price_per_day()}/day")

print()
print()