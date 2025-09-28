class Resturant:
    def __init__(self,rest_name,cuisine_type):
        self.rest_name=rest_name
        self.cuisine_type=cuisine_type
        
    def describe_resturant(self):
        print(f"Resturant name is {self.rest_name}")
        print(f"Cuisine served in the resturant is {self.cuisine_type}")
        
    def open_resturant(self):
        print(f"{self.rest_name} is open today!")
      
      
class IceCremeStand(Resturant):
    
    def __init__(self,rest_name,cuisine_type,flavour):
        super().__init__(rest_name,cuisine_type)
        self.flavour=flavour
        
    def show_flavour(self):
        print(f"These are the flavour u have requested")
        print(self.flavour)
        
        
rest1=IceCremeStand('kali ghata','all cuisine avilable',['dalda','mirch','patato'])
rest1.describe_resturant()
rest1.show_flavour()