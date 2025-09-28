class Users:
    
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        
    def describe_user(self):
        print(f"User name is {self.first_name} {self.last_name}")
        
    def greet_user(self):
        print(f"hello {self.first_name} {self.last_name}")
        
user1=Users('hasrh','tripathi')
user2=Users('rakesh','jhunjhun wala')
user3=Users('gopal','tiwari')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()