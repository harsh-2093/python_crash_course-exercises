#user_names=['harsh','admin','gopal','harshit','dev']

user_names=[]
if user_names:
    for user_name in user_names:
        if user_name=='admin':
            print(f"hello {user_name}. Would you like to see status report?")
        else:
            print(f"hello {user_name} thankyou for logginh in")
else:
    print("empty list")