def make_car(car_name,manufacturer,**other_info):
    
    other_info['Car_name']=car_name
    other_info['manufacturer']=manufacturer
    return other_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)