def make_album(artist_name, album_title, number_songs=None):
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if number_songs:
        album['number_of_songs'] = number_songs
    return album


while True:
    print("Enter 'q' at anytime to quit.")
    artist = input("Enter the artist's name: ")
    if artist == 'q':
        break
    title = input("Enter the album title: ")
    if title == 'q':
        break
    album = make_album(artist, title)
    print(album)
