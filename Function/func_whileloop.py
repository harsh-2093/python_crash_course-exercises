def formatted_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("to exit press q")
    first_name=input("enter first name")
    
    if first_name=='q':
        break
    last_name=input("enter last name")
    if last_name=='q':
        break
    name=formatted_name(first_name,last_name)
    print(f"hello {name}")