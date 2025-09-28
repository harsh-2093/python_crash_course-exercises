"""
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def get_descriptiv_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car=Car('audi','a4','2024')
print(my_new_car.get_descriptiv_name())
"""
#we add an attribut that change over time
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer} miles.")
        
    def update_odometer(self,mileage):
        if mileage >=self.odometer:
            self.odometer=mileage
        else:
            print("you cant roll back odometer")
    def increment_odometer(self,miles):
        self.odometer+=miles
"""
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
"""

#modyfing the attribute value

#1 approach 
"""
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer=23  #<--
my_new_car.read_odometer()
"""
"""
#2 approach
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(32)
my_new_car.read_odometer()
my_new_car.update_odometer(12)
my_new_car.read_odometer()

"""

#3 approach
# incermenting an attribute through method

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()