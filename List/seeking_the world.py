places=['haryana','dehradun','kerala','coorg','goa']
print(f"The original list: \n{places}")

print("\nalpha order list:")
print(sorted(places))

print("\noriginal list:")
print(places)

print("\nlist in reverse alpha order")
print(sorted(places,reverse=True))

print("\noriginal list:")
print(places)

places.reverse()
print(f"\nThe reverse list:\n{places}")

places.reverse()
print(f"\noriginal order using reverse():\n{places}")

places.sort()
print(f"\n the sorterd and stored list:\n{places}")

places.sort(reverse=True)
print(f"\nThe list in rev alpha order;\n{places}")