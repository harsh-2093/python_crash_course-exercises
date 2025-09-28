users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'priceton',
    },
    
    'mcurie': {
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
    
    
}

# now accessing the dict

for username,user_info in users.items():
    print(f"\n username:{username}")
    fullname=f"{user_info['first']} {user_info['last']}" # we are using f string to add to variable
    location=user_info['location']
    
    print(f"\t Full name:{fullname.title()}")
    print(f"\tLocation:{location.title()}")
    