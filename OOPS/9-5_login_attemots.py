class Users:
    
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
        
    def describe_user(self):
        print(f"User name is {self.first_name} {self.last_name}")
        
    def greet_user(self):
        print(f"hello {self.first_name} {self.last_name}")
    
    def incermenent_login_attempts(self):
        self.login_attempts+=1
        print(f"todays login {self.login_attempts}")

    
    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"todays login {self.login_attempts}")

        
user1= Users('gopal','tiwari')
user1.greet_user()
user1.incermenent_login_attempts()
user1.incermenent_login_attempts()
user1.incermenent_login_attempts()
user1.reset_login_attempts()

