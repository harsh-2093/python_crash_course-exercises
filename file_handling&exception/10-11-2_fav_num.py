from pathlib import Path

import json

path=Path('fav_number.json')

contents=path.read_text()
fav_nums=json.loads(contents)
print(f"Your favc_nums are: ")

for i in fav_nums:
    print(i)

