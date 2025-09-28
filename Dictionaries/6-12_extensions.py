fav_places={
    'gopal':['konch','beach','goa'],
    'bhadu':['konch','amethi'],
    'harsh':['uttarakhand','konch'],
}

#1 extension:adding morre info

fav_places['riya']=['mansoor','up']
fav_places['ramji']=['sasural']

fav_food={
    'gopal':['samosa','pizza','turai'],
    'bhadu':['chilli paneer','matha'],
    'harsh':['chawal','raita'],
    'riya':['paratha','tea','wine'],
    'ramji':['annar','burger'],
}

print("===Favorite Places===")
for name ,places in fav_places.items():
    print(f"Name:{name.title()} loves to go:")
    for place in places:
        print(f"\t{place.title()}")

print("===Fvorite Food===")
for name ,foods in fav_food.items():
    print(f"Name:{name.title()} loves to eat:")
    for food in foods:
        print(f"\t{food.title()}")