requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
"""
# simple for loop in list
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")
print("\nfinished making pizza")

"""

'''
# simple loop x=conisting if statement

for requested_topping in requested_toppings:

    if requested_topping=='green peppers':
        print("we are out of green peppers")
    else:
        print(f"adding {requested_topping}")
print("\nfinished makig your pizza")

'''
'''
#checking that the list is not empty
requested_toppings=[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"adding {requested_topping}")
        print("\n finished making your pizza")
else:
    print("are u sure u want plain pizza")

'''

#usig multiple list
avialable_topping=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']


for requested_topping in requested_toppings:
    if requested_topping in avialable_topping:
        print(f"adding {requested_topping}")
    else:
        print(f"not avilable:{requested_topping}")

print("pizza ready!")