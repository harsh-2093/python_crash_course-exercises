cities={
    'kanpur':{
        'country':'india',
        'population':10000000,
        'fact':'best leather product',
        },
    'sydney':{
        'country':'australia',
        'population':10000,
        'fact':'best falura and fauna',
        },
    'paris':{
        'country':'france',
        'population':10000,
        'fact':'best pizzas',
        },
}

for city , city_info in cities.items():
    print(f"City:{city.title()}\n\t Country:{city_info['country']} \tPopulation:{city_info['population']} \t Fact:{city_info['fact']}")
    