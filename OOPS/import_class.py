'''from module1_car import Car

my_new_car=Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()'''

'''# storing multiple class in module()

from module1_car import ElectricCar

my_leaf=ElectricCar('nissan','leaf',2014)

print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

'''

'''#importing multiple classes

from module1_car import Car,ElectricCar

my_mustang=Car('ford','mustang',2024)
print(my_mustang.get_descriptive_name())

my_leaf=ElectricCar('nissan','leaf',2024)
'''
#importing entire module()

import module1_car


my_mustang=module1_car.Car('ford','mustang',2024)
print(my_mustang.get_descriptive_name())

my_leaf=module1_car.ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
