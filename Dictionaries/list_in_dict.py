# store info about pizza being ordered
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    
}
# summarize te order
print(f"your ordered a {pizza['crust']} crust pizza")
for topping in pizza['toppings']:
    print(topping)

#2 eg

fav_lang={
    'jen':['python','rust'],
    'sarah':['c'],
    'edward':['rust','go'],
    'phil':['python','haskell'],

}
 # looping inside the dict and then looping through the values
for name,languages in fav_lang.items():
    print(f"{name.title()}'s lang is:")
    for lang in languages:
        print(f"\t{lang.title()}")
        
        