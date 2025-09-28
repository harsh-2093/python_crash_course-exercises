class Resturant:
    def __init__(self,rest_name,cuisine_type):
        self.rest_name=rest_name
        self.cuisine_type=cuisine_type
        
    def describe_resturant(self):
        print(f"Resturant name is {self.rest_name}")
        print(f"Cuisine served in the resturant is {self.cuisine_type}")
        
    def open_resturant(self):
        print(f"{self.rest_name} is open today!")
        
rest1=Resturant('momo jojo','chinese')
rest2=Resturant('zomatao','All cuisine avilable')
rest3=Resturant('hakka noodles','nepali')



rest1.describe_resturant()
rest1.open_resturant()


rest2.describe_resturant()
rest2.open_resturant()


rest3.describe_resturant()
rest3.open_resturant()