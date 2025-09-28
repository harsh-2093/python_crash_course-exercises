def make_pizza(size,*topping):
    print(f"making a {size}-inch pizza with the following toppings:")
    
    for i in topping:
        print(f"-{i}")