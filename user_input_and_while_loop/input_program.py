#1 input() take string as a value .

message=input("tell me something i will repeat it back:)")
print(message)
name=input("enter your name ")
print(f"\n hello,{name}")

# writing clear prompt

prompt="if you share your name , we can personalize the mess age you see"
prompt+="\n what is your name? "
name=input(prompt)
print(f"Hello,{name}")

#2 using int() to accept numerical input.


age =int(input("enter your age sir>?"))
if age>=18:
    print("U are eligible")
else:
    print("u re not eligoble")

height=(int (input("enter your height")))
if height>=48:
    print("\nYou're tall enough to ride!")
else:
    print("not boi this time")
    
    
# modulus operator(%) -->return reminader

number=int(input("enter the number"))
if number%2==0:
     print(f"{number} is even number")
else:
    print(f"{number} is not even number")
