motorcycle=['honda','yamaha','suzuki']
print(motorcycle)

#modification
motorcycle[0]='ducati'
print(motorcycle)

#adding element to the list

#1st method appending(adding item to the end of the list)
motorcycle.append('honda')
print(motorcycle)

friends=[]
friends.append('bhardwaj')
friends.append('gopal')
friends.append('himanshu')
print(friends)

#2nd inserting element to the list(after the index change all the values of the list shift to right side)
friends.insert(1,'dheeru')
print(friends)


# removing the item of list

#1 if we kno the position we use del statement 
grocery=['rajma','chawal','dal','sugar','chilli powder']
print(grocery)
del grocery[2]
del grocery[-1]
print(grocery)

#2 if you want to use the itemm after the deletion of the item we use pop() method
# pop() remove the last element from the list
stataes=['haryana','chandigarg','up','mp','punjab']
print(stataes)
poped_state=stataes.pop()
print(stataes)
print(poped_state)
poped_state=stataes.pop()
print(f"The last state that has been poped is {poped_state.title()}==mp")


#3 poping item from any position from list, we can user the pop ( )method by assigning the thge index int the pop(X)
brands=['tata','tyoyota','mahindra','aloo','samsung','apple']
print(brands)
poped_brands=brands.pop(3)
print(f"It is not abrand it is a sabji is {poped_brands}")

#4 remove the itme by using values remove()

books=['maths','chemistry','python','hindi','english']
print(books)
cs_book='python'
books.remove(cs_book)
print(books)
print(f"this is the most expensive book {cs_book}")
