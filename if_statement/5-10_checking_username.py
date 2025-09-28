current_users=['harsh','vaibhav','karan','yash','mukesh']

new_users=['dinesh','karan','gaurav','harsh','jay']

for new_user in new_users:
    if new_user in current_users:
        print(f"this username {new_user} is not avialable")

    else:
        print(f"{new_user} user name is avilable")