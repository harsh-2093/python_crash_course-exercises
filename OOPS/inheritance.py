class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery:
    def __init__(self,battery_size=40):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"this car has a {self.battery_size}-kwh battery.")
    def get_range(self):
        if self.battery_size==40:
            range=150
        elif self.battery_size==56:
            range=225
        print(f"This car can go about {range} miles on full charge")
        
        
        
     
'''class ElectricCar(Car):

    """represent aspect of car, specific to electric vehicles"""
    
    def __init__(self,make,model,year):
        """initialize attributes of parent car"""
        super().__init__(make,model,year)
        self.battery_size=40
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
    def fill_gas_tank(self):
        print("this car dosent have gas tank!")
        
'''

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
        
        
        
"""
my_leaf=ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
"""            
######---->Defining Attributes and Methods for the Child Class
my_leaf=ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.battery_size=56
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()


#modeling real world object
