#simple if statement 
age=18

if age>=18:
    print("u can vote")
    print("have u regestired ur vote yet?")


#if_else statement
age=20

if age>=18:
    print("u can vote")
    print("have u regestired ur vote yet?")
else:
    print("u are too younger")
    print("register ur vote when u turn 18")


"""
# if-elif-else chain
age=18

if age<4:
    print("your ticket is free")
elif age<18:
    print("your fare is 25$")
else:
    print("ur fare is 40$")
"""
    #OR
age =45
if age<4:
    price=0
elif age<18:
    price=25
else:
    price=40

print(f"your price is {price}$")

# using multiple if blocks
age =45
if age<4:
    price=0
elif age<18:
    price=25
elif age>65:
    price=20
else:
    price=40

print(f"your price is {price}$")

#omitting of else block

age=90

if age<4:
    price=4
elif age<18:
    price=25
elif age<65:
    price=45
elif age>=65:
    price=20

print(f"your admission price ={price}$")

#testing multiple condition-> by working of multiple check prefer to use if statment only:

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("adding mushroms")
if 'pepperoni' in requested_toppings:
    print("adding pepperonio")
if 'extra cheese' in requested_toppings:
    print("adding cheese")
print("finisdhes making your pizza")

""" In summary, if you want only one block of code to run, use
an if-elif-else chain. If more than one block of code needs
to run, use a series of independent if statements"""