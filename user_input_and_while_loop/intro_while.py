"""
currne_number=1
while currne_number<=5:
    print(currne_number)
    currne_number+=1

#2 letting the user to quit the program
prompt="\n tell me something ill repeatback to u: "
prompt+="\n enter 'quit' to end program. "

message=""
while message !='quit':
    message=input(prompt)
    if message!='quit':
        print(message)

#3  using the flag in while to stop program

prompt="\n tell me something ill repeatback to u: "
prompt+="\n enter 'quit' to end program. "
active=True

message=""
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)
        
        
#4 using break statement to stop while
prompt="\n tell me something ill repeatback to u: "
prompt+="\n enter 'quit' to end program. "
while True:
    city=input(prompt)
    if city=='quit':
        break
    else:
        print(f"i'd love to go {city}")
"""
#5 using continue in loop
# consider a loop that counts from 1 to 10 but prints only the odd numbers in that range:
current_number=0

while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)

#6 avoiding infinite loop
