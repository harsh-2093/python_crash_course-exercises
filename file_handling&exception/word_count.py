from pathlib import Path

def count_words(path):
    try:
        content=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
        #print(f"sorry, the file {path} does not exist")
    else:
        words=content.split()
        num_count=len(words)
        print(f"The file {path} has about {num_count} words!")


filename=['alice.txt','alice1.txt','harsh.txt','alice2.txt']

for i in filename:
    path=Path(i)
    count_words(path)