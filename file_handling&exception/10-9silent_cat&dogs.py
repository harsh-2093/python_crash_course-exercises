from pathlib import Path

files=['cat.txt','dog.txt','SF.TXT']

for i in files:
    path=Path(i)
    try:
        content=path.read_text()
    except FileNotFoundError:
        pass
    else:
        lines=content.splitlines()
        for i in lines:
            print(i)