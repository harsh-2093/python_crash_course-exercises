from pathlib import Path

path=Path('multilple_line.txt')

content="i love programming.\n"
content+="i lov-e gaming.\n"
content+="i love cooking. \n"

path.write_text(content)