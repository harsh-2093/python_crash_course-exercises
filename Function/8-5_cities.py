def describe_city(name,country='india'):
    print(f"{name.title()} is in {country.title()}")
    
describe_city(name='goa')
describe_city('haryana')
describe_city('tokyo','japan')