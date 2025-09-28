#1 usi

while True:
    
    age=input("enter your age")
    if age=='quit':
        break
    print(f"your age is {age}")
    if int(age)>18 :
        print("you are adult")
    else:
        print("you are child")