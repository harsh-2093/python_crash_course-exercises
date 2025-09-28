from user1 import Users
from priv_and_admin import Admin as ad

user1=Users('harsh','tripathi')
user1.greet_user()

user2=ad('gopal','Tiwari')
user2.greet_user()
user2.privilages.show_privileges()