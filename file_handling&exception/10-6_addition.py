try:
    first_number=int(input("enter the number"))
    second_number=int(input("enter the number"))
except ValueError:
    print("please provide the numeric data!")
    
else:
    result=first_number+second_number
    print(result)