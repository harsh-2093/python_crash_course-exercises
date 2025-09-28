from pathlib import Path

path=Path('learning_python.txt')

contents=path.read_text()

lines=contents.splitlines()


for i in lines:
    print(i.replace('python','C'))
    
