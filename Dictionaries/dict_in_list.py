#1 nesting: a list of dictinory
 
 # first we intialize dict
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}

 # now we make the list of these dict
aliens=[alien_0,alien_1,alien_2]

 # we can access the alien by loop for :
for alien in aliens:
    print(alien)
 # alt method
aliens=[]

for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
 # now show the first five aliens
for i in aliens[:5]:
    print(i)
print("...")

 # show how many alien hve been created 
print(f"Total no of aliens:{len(aliens)}")

#For example, to change the first three aliens to yellow, mediumspeed aliens worth 10 points each, we could do this:
aliens=[]
for alien in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if  alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'
 # showing first 5 alien
for alien in aliens[:2]:
    if alien['color']=='yellow':
        alien['color']='red'
        alien['points']=15
        alien['speed']='fast'
for alien in aliens[:5]:
    print(alien)