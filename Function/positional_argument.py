def describe_pet(animal_type,pet_name):
    """display info about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name.title()}.")
    
describe_pet('hamster','harry_Putra') #positional_argument


describe_pet('dog','wallahy')#multiple function call

#mixing up the order in posn argument
#describe_pet('harry', 'hamster')

