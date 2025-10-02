from pathlib import Path

import json
def get_stored_username(path):
    """get the stored username"""
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    username=input("enter the name")
    contents=json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name"""
    path=Path('username.json')
    username=get_stored_username(path)
    if username:
        print(f"Wlecome {username}")
    else:
        username=get_new_username(path)
        print(f"we'll remember you ! ,{username}") 

greet_user()   