# eg of dict in list
person_1={
    'first_name':'gopal',
    'last_name':'tiwari',
    'age':19,
    'city':'konch',
}
person_2={
    'first_name':'harsh',
    'last_name':'tripathi',
    'age':19,
    'city':'kanpur',
}

people=[person_1,person_2]

for person in people:
    full_name=f"{person['first_name']} {person['last_name']}"
    print(f"User:{full_name}")
    print(f"\t age={person['age']} city={person['city']}")
