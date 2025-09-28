fav_places={
    'gopal':['konch','beach','goa'],
    'bhadu':['konch','amethi'],
    'harsh':['uttarakhand','konch'],
}

for name ,places in fav_places.items():
     print(f"Name:{name}")
     for place in places:
         print(f"\t{place}")