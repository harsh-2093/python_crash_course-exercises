from pathlib import Path

import json

def input_dict():
    dicto={}
    print("enter your dict, enter q to exit")
    while True:
        word=input("enter the word: ")
        if word =='q':
            break
        meaning=input(f"Enter the mening of {word}: ")
        if meaning=='q':
            break
        dicto[word]=meaning
    return dicto 

path=Path('dictanary.json')

if path.exists():
    contents=path.read_text()
    dicto=json.loads(contents)
    for i,j in dicto.items():
        print(f"{i}:{j}")       
else:
    dicto=input_dict()
    contents=json.dumps(dicto,indent=4)
    path.write_text(contents)