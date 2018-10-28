def make_album(singer_name, album_name, songs_num=''):
    album = {'singername:': singer_name,'album_name': album_name}
    if songs_num:
        album['song_num'] = songs_num 
    return album
print(make_album('abel', 'aaa', 10))
print(make_album('zhou', 2333))
