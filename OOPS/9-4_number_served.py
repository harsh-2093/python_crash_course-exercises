class Resturant:
    def __init__(self,rest_name,cuisine_type,):
        self.rest_name=rest_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        
    def describe_resturant(self):
        print(f"Resturant name is {self.rest_name}")
        print(f"Cuisine served in the resturant is {self.cuisine_type}")
    def numbers(self):
        print(f"no of serving are {self.number_served}")
        
    def open_resturant(self):
        print(f"{self.rest_name} is open today!")
        
    def set_number_served(self,num):
        self.number_served=num
    def increment_number_served(self,n2):
        self.number_served+=n2
        
rest1=Resturant('momo jojo','chinese')


rest1.describe_resturant()
rest1.numbers()


rest1.number_served=34
rest1.numbers()

rest1.set_number_served(43) 
rest1.numbers()

rest1.increment_number_served(14)
rest1.numbers()