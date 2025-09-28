pizzas=['onion_pizza','paneer_pizza','dal_pizza']
friend_pizza=pizzas[:]
pizzas.append('kathal_pizza')
friend_pizza.append('desi pizza')

print("my fav pizza list are:\n")
for pizza in pizzas[:]:
    print(pizza)

print("\n list of my friend pizza list:\n")
for pizza in friend_pizza[:]:
    print(pizza)