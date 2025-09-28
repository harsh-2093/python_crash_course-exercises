from pathlib import Path

path=Path('guests.txt')

guests=int(input("enter the no of guests. 0 for no guests: "))
list_guests=""
while guests:
    name=input("enter the name: ")
    list_guests+=name +"\n"
    guests=guests-1
path.write_text(list_guests)