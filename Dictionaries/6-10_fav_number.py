fav_number={
    'harsh':[9,3.6],
    'gopal':[4,2,7],
    'rajesh':[7,7],
    'ishan':[6],
    'gupta':[3,89],
}

for name ,numbers in fav_number.items():
    print(f"Name:{name}")
    for number in numbers:
        print(f"\t{number}")