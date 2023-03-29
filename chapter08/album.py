def make_album(artist_name, album_title, number_songs=None):
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if number_songs:
        album['number_of_songs'] = number_songs
    return album


print(make_album('miley cyrus', 'endless summer vacation'))
print(make_album('taylor swift', 'red'))
print(make_album('dermot kennedy', 'sonder', 11))
