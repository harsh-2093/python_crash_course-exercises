class Users:
    
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        
    def describe_user(self):
        print(f"User name is {self.first_name} {self.last_name}")
        
    def greet_user(self):
        print(f"hello {self.first_name} {self.last_name}")
        
class Privileges():
    def __init__(self,power=['Can add post','Can delete post','Can ban user']):
        self.power=power    
        
        
    def show_privileges(self):
        print("These are the privilages of Admin")
        
        for i in self.power:
            print(f"{i}")
            
        
    
        

class Admin(Users):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privilages=Privileges()     
        
        
admin1=Admin('harsh','tripathi')
admin1.describe_user()
admin1.privilages.show_privileges()