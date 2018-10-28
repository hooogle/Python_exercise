def make_album(singer_name, album_name, songs_num=''):
    album = {'singername:': singer_name,'album_name': album_name}
    if songs_num:
        album['song_num'] = songs_num 
    return album
while True:
    print("Please tell me the info about albums\nYou can input 'q' at any time to quit.")
    singer_name = input('singer_name: ')
    if singer_name == 'q':
        break
    album_name = input('album_name: ')
    if album_name == 'q':
        break
    songs_num = ''
    if input('Do you know how many songs in this albun(yes/no)? ') == 'yes':
        songs_num = int(input("songs_num: "))
        if str(songs_num) == 'q':
            break
    print(make_album(singer_name, album_name, songs_num))
    


    
