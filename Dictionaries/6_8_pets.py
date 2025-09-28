pet_1={
    'animal':'dog',
    'owner':'harsh',
    'age':2,
}

pet_2={
    'animal':'cat',
    'owner':'rashmi',
    'age':4,
}

pet_3={
    'animal':'parrot',
    'owner':'piyush',
    'age':6,
}

pets=[pet_1,pet_2,pet_3]

for pet in pets:
    print(f"Animal:{pet['animal']} \n\tOwner:{pet['owner']}  Age:{pet['age']}")
    