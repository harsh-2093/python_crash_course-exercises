# tuple = immutable list is called tuple(its inside data cannot be modify or change)
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

print("\n")
#2 looping inside the tuple
for dimension in dimensions:
    print(dimension)

#3 writing over the tuple(we couldnt change the dimension of the tuple but we can redefine the whole tuple)
new_archieves=(200,50)
print("\noriginal dimension:")
for i in new_archieves:
    print(i)
print("\nnew dimension")
new_archieves=(145,69)
for i in new_archieves:
    print(i)

#Use them when you want to store a set of values that should not be changed throughout the life of a program.