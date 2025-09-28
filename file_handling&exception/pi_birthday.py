from pathlib import Path

path=Path('pi_one_million_.txt')

contents=path.read_text()

lines=contents.splitlines()
print(lines)

pi_string=''

for line in lines:
    pi_string+=line.strip()
    
birthday=input("Enter your bithday,in form of mmddyy: ")

if birthday in pi_string:
    print("Your birthday appear in first 1 10lakh decimal of pi")
    
else:
    print("it does not")
print(pi_string)
print(len(pi_string))