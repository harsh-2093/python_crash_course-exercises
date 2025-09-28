def make_album(artist_name,album_title,no_song=None):
    album={
        'Name':artist_name,
        'Title':album_title,
    }
    if no_song:
        album['No_of_song']=no_song
    return album

album=make_album('Harsh','Lapata',90)
print(album)
album=make_album('yogi','up')
print(album)
album=make_album('jeetu','AI (andal intelligence)',8)
print(album)


