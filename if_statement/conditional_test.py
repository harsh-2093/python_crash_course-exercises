#1 checking for eqaulity ==

name='harsh'
print(name=='rabish')
print(name=='harsh')
print(name=='HARSH')
print(name.upper()=='HARSH')
print(name)

#2 che4cking for inequality !=
requested_topping='mushrooms'

if requested_topping!='mushrooms':
    print("\nchl be chakke")


#3 numerical comparisons
answer=58
if answer!=57:
    print(f"{answer} it is not correct")
else:
    print("yes it is cvorrecxt")

print(answer<100)
print(answer>60)
print(answer<=58)

print("\n")


#4 checking multiple condition --> use of and(&&) or(||)

#4.1 using and
age_0=22
age_1=34
print(age_0>=21 and age_1>=21)

#4.2 using or
age_0=22
age_1=18
print(age_0>=21 or age_1>=21)

print('\n')


#5 checking wether the value is in the list
# we use keyword in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('peppreroonis' in requested_toppings)

print('\n')

#6 Checking Whether a Value Is Not in a List
# we use keyword not
banned_users = ['andrew', 'carolina', 'david']
user='marie'
if user not in banned_users:
    print(f"{user.title()} you can post resopnse if u wish to")


#7 boolean e1xpression
#just another NAME OF CONDITIONAL STATEMENT