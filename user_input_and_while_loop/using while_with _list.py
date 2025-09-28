"""
#Moving Items from One List to Another

unconfirmed_users=['alice','brain','candace']
confirmed_users=[]

while unconfirmed_users:
    current_users=unconfirmed_users.pop()
    print(f"verifying user: {current_users.title()}")
    confirmed_users.append(current_users)
    
print("thse are confirmed user: ")

for i in confirmed_users:
    print(i.title())
    
#2 Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
 pets.remove('cat')
print(pets)
"""
#3 Filling a Dictionary with User Input

responses={}

polling_active=True

while polling_active:
    name=input("\n enter your name ")
    response=input("which mountain u like to climb someday ? ")
    
    responses[name]=response
    
    repeat=input("would you like to letanother person response?(yes/no)")
    
    if repeat=='no':
        polling_active=False
print("---poll results---")
for name , response in responses.items():
    print(f"{name} would like to climb {response}.")