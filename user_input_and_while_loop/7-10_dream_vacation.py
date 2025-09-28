responses={}

polling_active=True

while polling_active:
    name=input("enter your name")
    place=input("enter the place you want to explore")
    
    responses[name]=place
    
    
    respond=input("would you like to let other person resopnd yes/no")
    
    if respond=="no":
        polling_active=False
        

for name,pl in responses.items():
    print(f"{name.title()} want to explore {pl.title()}")
    
     