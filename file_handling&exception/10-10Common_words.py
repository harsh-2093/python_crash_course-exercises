from pathlib import Path

path=Path('Enviroment.txt')

content=path.read_text()

print(content.lower().count('the '))