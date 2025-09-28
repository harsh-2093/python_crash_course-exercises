#returning the simple value
def get_fullname(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title() #return statement

musician=get_fullname('jimmy jimmmy','aja aja aja')
print(musician)

#basic func with return statement 

#making an argument optional

def get_formatted_name(first_name, last_name, middle_name=""):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {middle_name} {last_name}"
 return full_name.title()
musician = get_formatted_name('john','hooker')
print(musician)
musician=get_formatted_name('harsh','tripathi',middle_name='dala')
print(musician)