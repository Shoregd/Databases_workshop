from lib.album import Album

def test_init_correct():
    test_album = Album(1,'Test Title',1989,1)
    assert test_album.id == 1
    assert test_album.title == 'Test Title'
    assert test_album.artist_id == 1
    assert test_album.release_year == 1989

def test_album_format():
    test_album = Album(1,'Test Title',1989,1)
    assert str(test_album) == 'Album(1, Test Title, 1989, 1)'

def test_albums_equal_classes():
    test_album = Album(1,'Test Title',1989,1)
    test_album2 = Album(1,'Test Title',1989,1)
    assert test_album == test_album2