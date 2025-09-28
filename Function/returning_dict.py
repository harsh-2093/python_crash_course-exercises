def build_person(first_name,last_name,age=None):
    person={
        'first':first_name,
        'last':last_name,
        
    }
    if age:
        person['age']=age
    return person
muscian=build_person('hasrh','tripathi',19)
print(muscian)