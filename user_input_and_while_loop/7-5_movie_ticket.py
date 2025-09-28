while True:
    age=input("enter your age.")
    
    if age=='quit':
        break
    else:
        if int(age)<3:
            print("ticket is free")
        elif int(age)>=3 and int(age)<12:
            print("your fare is $10")
        else:
            print("your fare is $15")