from pathlib import Path

import json


path=Path('user.json')

if path.exists():
    contents=path.read_text()
    user=json.loads(contents)
    current_user=input("enter yourt name: ")
    if(current_user==user):
        print(f"Welcome_back {user}")
    else:
        username=input("enter ypur name: ")
        contents=json.dumps(username)
        path.write_text(contents)
else:
        
    username=input("enter ypur name: ")
    contents=json.dumps(username)
    path.write_text(contents)

