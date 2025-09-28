'''print(5/0) '''##-> creating an zerodivision error 

# using try-except blocks


try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by Zero!")
