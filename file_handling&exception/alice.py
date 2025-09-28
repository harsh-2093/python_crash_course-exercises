#Handling the FileNotFoundError Exception

from pathlib import Path

path=Path('alice.txt')
try:
    content=path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("no such file exists")
else:
    words=content.split()
    num_words=len(words)
    print(f"The file {path} has about {num_words} words.")