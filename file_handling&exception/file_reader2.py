"""#accessing files lines
from pathlib import Path

path=Path('pi_digits.txt')
contents=path.read_text()
lines=contents.splitlines()
print(lines)

for line in lines:
    print(line)"""
    

#working with files constant's

from pathlib import Path

path=Path('pi_one_million_.txt')
contents=path.read_text()


lines=contents.splitlines()

pi_string=''
for i in lines:
    pi_string+=i.lstrip()
    
print(f"{pi_string[:52]}....")
print(len(pi_string))
    
