def user_profile(first_name,last_name,**info):
    info['first_name']=first_name
    info['last_name']=last_name
    print(f"user_info of Mr{first_name.title()}{last_name.title()}")

    for i,j in info.items():
        print(f"{i}:{j}")
    
user_profile(first_name='lalu',last_name='prashad',age=69,color='chatak lal')

user_profile(first_name='bhindi',last_name='singh',age=68,color='chatk neeli')
