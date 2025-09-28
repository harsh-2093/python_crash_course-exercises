#1 use of * (when we dont know how many argument are there)
# * asterik in parameter tell ptyhton to make tuplecalled topping cointain all value func recieve
"""
def make_pizza(*topping):
    print(topping)
    
make_pizza('pepperoni')
make_pizza('mushroom','green pepperrs','extra cheese')
"""
# o/p
# ('pepperoni',)
#('mushroom', 'green pepperrs', 'extra cheese')

#we can use loop also 
def make_pizza(*topping):
    print("making pizza with refered toppings:")
    for i in topping:
        print(f"\t{i}")
    
make_pizza('pepperoni')
make_pizza('mushroom','green pepperrs','extra cheese')

#Mixing Positional and Arbitrary Arguments