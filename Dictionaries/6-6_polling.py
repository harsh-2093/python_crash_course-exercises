favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_poll=['jen','edward','michael', 'sarah', 'emma','phil']

for people in people_to_poll:
    if people in favorite_languages.keys():
        print(f"{people} thanks for your respond !")
    else:
        print(f"{people} u are invited for poll!")