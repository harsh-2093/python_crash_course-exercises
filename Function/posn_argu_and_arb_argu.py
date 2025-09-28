#If you want a function to accept several different kinds of arguments,
# the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.
"""
def make_pizza(size,*topping):
    print(f"pizza size of {size} with refered topping being ready!")
    for i in topping:
        print(f"\t{i}")
    
make_pizza(12,'pepperoni')
make_pizza(7,'mushroom','green pepperrs','extra cheese')
"""

#Using Arbitrary Keyword Arguments
# ** cretae the dict of as mamy key word /value
def builf_profile(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile=builf_profile('albert','einstein',
                           place='princetown',
                           subject='physics')
print(user_profile)

