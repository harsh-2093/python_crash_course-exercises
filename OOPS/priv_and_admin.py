from user1 import Users
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
        
 