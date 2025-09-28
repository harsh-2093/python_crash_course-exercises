# organisising list

#1 sorting using sorting method()
# we can't revert the original order
cars=['honda','suzuki','tyota','mazda']
print(cars)
cars.sort()
print (cars)
#1.1 can also store list in reverse alpha order
# using reverse=true
cars.sort(reverse=True)
print(cars) 

#2 now sorting the list temporary using sorted() function
cars=['honda','suzuki','tyota','mazda']
print("\nhere the originbal list")
print(cars)

print("\n here the sorted carts")
print(sorted(cars))

print("\n here the original list again")
print(cars)
#2.1 it also can store reverse alpha order

print("\n reverse alpha order\n")
print(sorted(cars,reverse=True))

#3 printing the list in thr reverse order
#using reverse() method

carz = ['bmw', 'audi', 'toyota', 'subaru']
print("\n")
print(carz)

print ("\nthe cas in reverse order")
carz.reverse()
print(carz)

#4 Finding the length of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))