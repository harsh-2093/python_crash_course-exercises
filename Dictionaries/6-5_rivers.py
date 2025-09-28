rivers={
    'nile':'egypt',
    'ganga':'india',
    'yamnuna':'india',
}
for river,country in rivers.items():
    print(f"The {river.title()} run through {country.title()}")
for river in rivers:
    print(f"{river}")
for country in rivers.values():
    print(f"{country}")