"""#
def greet_user(names):
    for name in names:
        msg=f"hello,{name.title()}"
        print(msg)
usernames=['harsh','tripathi']
greet_user(usernames)

#modyfying list in a function
unprinted_designs=['phone case','robot pendant','dedecahedron']
completed_models=[]

while unprinted_designs:
    current_design=unprinted_designs.pop()
    print(f"printing model:{current_design}")
    completed_models.append(current_design)
    
print("\n the following model have been printted")

for i in completed_models:
    print(i)
    
# writting the upper model in different momdel

def print_model(unprinted_designs,completed_designs):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(current_design)
        completed_models.append(current_design)        
def completed_design(completed_models):
    for i in completed_models:
        print(i)
        

unprinted_designs=['phone case','robot pendant','dedecahedron']
completed_models=[]
print_model(unprinted_designs,completed_models)
completed_design(completed_models)

"""
#preventing a func to modify list

