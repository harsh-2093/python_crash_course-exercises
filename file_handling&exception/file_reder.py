'''#reading the contents fro the file

from pathlib import Path

path=Path('pi_digits.txt')
contents=path.read_text().rstrip()
print(contents)'''

r'''#realtive and absolute __path__ upper was a relative path
from pathlib import Path

#absolute path
path=Path(r'C:\Users\hemla\OneDrive\Desktop\C_language\b.txt')

contents=path.read_text()
print(contents)'''
'''Windows systems use a backslash (\) instead of a
forward slash (/) when displaying file paths, but you
should use forward slashes in your code, even on
Windows. The pathlib library will automatically use the
correct representation of the path when it interacts
with your system, or any user’s system.
'''
#accessing files lines
from pathlib import Path

path=Path(r'pi_digits.txt')
contents=path.read_text()
lines=contents.splitlines()

for line in lines:
    print(line)