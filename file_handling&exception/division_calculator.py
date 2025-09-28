print("give me two numbers and i'll divide them.")
print("enter q to quit")

while True:
    first_number=input("\nFirst number: ")
    if first_number=='q':
        break
    second_number=input("\nSecond number: ")
    if second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you an't divide ny 0!")
    else:
        print(answer)
    