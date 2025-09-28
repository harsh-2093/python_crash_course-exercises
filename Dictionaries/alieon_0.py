alien_0={'color':'green','points':5}


# REAL WORLD SOLN WITH DICTATIONARY
# A key’s value can be a number, a string, a list, or even another dictionary.

# 1 accessing values in dictionary
print(alien_0['color'])
print(alien_0['points'])
print(f"you just earned {alien_0['points']} points.")

#2 adding the new key-value pairs
# before
print(alien_0)

# after
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#3 starting with an empty dictionary
alien_0={}

alien_0['color']='green'
alien_0['point']='5'
alien_0['position']='centre'

print(alien_0)

#4 modyfying values in dictionary
# we are changing the value of green to yellow
# before
print(f"the alien before color is {alien_0['color']}")
alien_0['color']='yellow'

print(f"the alien after color is { alien_0['color']}")

# more example 
alien_0={'x_position':0,'y_position':'25','speed':'medium'}
print(f"original position= {alien_0['x_position']}")

#move the alien to the right
#determine how far to move the alien on its current speed

#4.1
# alien_0['speed']='fast'
if alien_0['speed']=='slow':
    x_incerment=1
elif alien_0['speed']=='medium':
    x_incerment=2
else:
    # this must be a fast alien
    x_incerment=3
# the new positioon is the old position plus the inbcrement.
alien_0['x_position']=alien_0['x_position']+x_incerment

print(f"the new position of the alien is {alien_0['x_position']}")


#5 removing the key value pair
#removing the speed in alien_0

del alien_0['speed']
print(alien_0)

#Note Be aware that the deleted key-value pair is removed permanently.

#6 dictionary of similar object
#fav_language
favourite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'pyhton',
}
langauage=favourite_language['sarah'].title()
print(f"sarah fav language is {langauage}")

#7 using get()to access values
alien_0 = {'color': 'green', 'speed': 'slow'}
# if the key is not present it return key error:

# best method to use is get()
point_value=alien_0.get('points','no point value assigned')

print(point_value)