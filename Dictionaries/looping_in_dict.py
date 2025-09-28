#1 looping through key and value pair

#several different ways exist to loop through them dict
# can be loop through its keys, or through its values.

user_0={
    'username':'efermi',
    'first':'enrico',
    'lastname':'fermi',
}

# in for loop we use items() which return key value pair:
# eg 1
for key,value in user_0.items():
    print(f"\nkey:{key}")
    print(f"value:{value}")
# eg 2
fav_lang={
    'harsh':'c',
    'gopal':'python',
    'bhadu':'hindi',
}

for name , lang in fav_lang.items():
    print(f"{name} love {lang}")

#"This type of looping would work just as well if our dictionary stored the results from polling a thousand or even a million people"

#2 looping through all the keys in dictionary

# when we don't need the value we use this method

fav_lang={
    'harsh':'c',
    'gopal':'python',
    'bhadu':'hindi',
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}


# print all the user who took poll "we use .keys()"
for key in fav_lang.keys():
    print(f"{key.title()}! thanks for your response.")
# note looping through keys is default in dict

print("\nxxx\n")
friends=['harsh','bhadu','phil']
for name in fav_lang.keys():
    print(f"hi {name.title()}")

    if name in friends:
        language=fav_lang[name]
        print(f"\t{name.title()} i see you love {language}")

# checking whether the person is in dict or not

if 'erin' not in fav_lang.keys():
    print("erin pls take our poll")

print("\nxxx\n")
#3 Looping Through a Dictionary’s Keys in a Particular Order


# in this we have use sorted() func which does not excatly change the order but but making the copy and arrange in sorted manner it arranges

for name in sorted(fav_lang.keys()):
    print(f"{name} thanks for poll")

print("\nxxx\n")

#4 looping through all the values in dict

print("following lang have been choosen")
for value in fav_lang.values():
    print(f"{value}") # print all the value in dict
print(" ")
# there is one drawback in using this method ,it work fine with small number of values ,but in large no of poll or value  it result in repetitive list , to see each lang choosen without repetition we use set.
#set:A set is a collection in which each item must be unique.
for value in set(fav_lang.values()):
    print(f"{value}")
print("\nxxx\n")

### building set
lang={'python','c','python','rust','c'}
print(lang)

