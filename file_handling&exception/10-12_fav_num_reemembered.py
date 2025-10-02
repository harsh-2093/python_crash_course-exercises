from pathlib import Path

import json

def fav_numbers():
    fav_nums=[]
    while True:
        print("enter the number to quit enter q")
        number=input("enter the number")
        if number=='q':
            break
        fav_nums.append(int(number))
    return fav_nums


path=Path('fav_number.json')
if path.exists():
    contents=path.read_text()
    fav_nums=json.loads(contents)
    print(f"Your favc_nums are: ")
    for i in fav_nums:
        print(i)
else:
    contents=json.dumps(fav_numbers())
    path.write_text(contents)
    
    
    
    



    
    