def make_album(artist_name,album_title,no_song=None):
    album={
        'Name':artist_name,
        'Title':album_title,
    }
    if no_song:
        album['No_of_song']=no_song
    return album


while True:
    print("Enter the info of album")
    print("to exit enter q")
    
    name=input("enter your name")
    if name=='q':
        break
    title_album=input("enter title of song ")
    if title_album=='q':
        break
    no_of_song=int(input("enter the no of song _if N/A enter 0"))
    if no_of_song==0:
        no_of_song=None
    result=make_album(name,title_album,no_of_song)
    print(result)


