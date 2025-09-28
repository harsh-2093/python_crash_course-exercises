number=69

print("i think its false",number==70)
print("i think its true",number==69)
print("i think its true",number<=70)
print("i think its false",number>=70)
print("i think its true",number!=70)

#5-2 more condition test
random_items = ["guitar", "pizza", "moonlight", "robot", "jungle"]
if 'guitar' in random_items:
    print("\nyes it is")
else:
    print("not")

if 'Guitars' not in random_items:
    print("\nyes it is not in list")
else:
    print("not")

item='guitar'
for i in random_items:
    if i .lower()==item:
        print('yes hai re bidu')