class Dog:
    """a simple attempt to  model a dog"""
    
    def __init__(self,name,age):
        """initialize name and age attribute."""
        self.name=name
        self.age=age
    
    def sit(self):
        """simulate a dog sitting  in response to a  command"""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """simulate rolling over in response to command"""
        print(f"{self.name} rolled over !") 
        
        
#making instances
my_dog=Dog('willie',6)
your_dog=Dog('lucy',3)

print(f"my dog name is {my_dog.name}")
print(f"my dog age is {my_dog.age}")
my_dog.sit()

print(f"your dog name is{your_dog.name}")
print(f"your dog name is {your_dog.age}")
your_dog.sit()