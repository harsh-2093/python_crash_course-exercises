players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())

#copying a list[]
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods=my_foods[:]           #<--copying list[]  also both variable point to different list

print(f"tis is my list {my_foods}")
print(f"\ntis is my friend list {friend_foods}\n")

#wrong method
numbers=[value for value in range(0,11)]
new_numbers=numbers

numbers.append('hijru')        #
new_numbers.append('bois')     #both variable pointing to same list 
print(numbers)                 #
print(new_numbers)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hijru', 'bois']
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hijru', 'bois']
