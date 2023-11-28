from lib.album_repository import AlbumsRepository
from lib.album import Album


def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumsRepository(db_connection) # Create a new ArtistRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album(1,'Doolittle',1989,1),
        Album(2,'Surfer Rosa',1988,1),
        Album(3,'Waterloo',1974,2),
        Album(4,'Super Trouper',1980,2),
        Album(5,'Bossanova',1990,1),
        Album(6,'Lover',2019,3),
        Album(7,'Folklore',2020,3),
        Album(8,'I Put a Spell on You',1965,4),
        Album(9,'Baltimore',1978,4),
        Album(10,'Here Comes the Sun',1971,4),
        Album(11,'Fodder on My Wings',1982,4),
        Album(12,'Ring Ring',1973,2)
    ]

def test_find_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumsRepository(db_connection) # Create a new ArtistRepository
    assert repository.find(6) == Album(6,'Lover',2019,3)

'''
Test-drive a create method for your AlbumRepository class.
Test-drive a delete method for your AlbumRepository class.
'''
'''
    add_album(self,art_id,album_title,release_yr): take the information and create
    a new record in the albums table executing
    'INSERT INTO albums (title,release_year,artist_id) VALUES(%s,%s,%s), [album_title,release_yr,art_id]
    delete_album(album_id): remove specified album from album list executing
    'DELETE FROM albums WHERE id = %s', [album_id]
'''


def test_user_can_create_album(db_connection):
    db_connection.seed("seeds/music_library.sql") 
    repository = AlbumsRepository(db_connection)
    repository.add_album(1,'Rock Around The Pixies Clock',2023)
    result = repository.all()
    assert result == [
         Album(1,'Doolittle',1989,1),
        Album(2,'Surfer Rosa',1988,1),
        Album(3,'Waterloo',1974,2),
        Album(4,'Super Trouper',1980,2),
        Album(5,'Bossanova',1990,1),
        Album(6,'Lover',2019,3),
        Album(7,'Folklore',2020,3),
        Album(8,'I Put a Spell on You',1965,4),
        Album(9,'Baltimore',1978,4),
        Album(10,'Here Comes the Sun',1971,4),
        Album(11,'Fodder on My Wings',1982,4),
        Album(12,'Ring Ring',1973,2),
        Album(13,'Rock Around The Pixies Clock',2023,1)
    ]
def test_user_can_delete_album(db_connection):
    db_connection.seed("seeds/music_library.sql") 
    repository = AlbumsRepository(db_connection)
    repository.add_album(1,'Rock Around The Pixies Clock',2023)
    repository.delete_album(13)
    result = repository.all()
    assert result == [
        Album(1,'Doolittle',1989,1),
        Album(2,'Surfer Rosa',1988,1),
        Album(3,'Waterloo',1974,2),
        Album(4,'Super Trouper',1980,2),
        Album(5,'Bossanova',1990,1),
        Album(6,'Lover',2019,3),
        Album(7,'Folklore',2020,3),
        Album(8,'I Put a Spell on You',1965,4),
        Album(9,'Baltimore',1978,4),
        Album(10,'Here Comes the Sun',1971,4),
        Album(11,'Fodder on My Wings',1982,4),
        Album(12,'Ring Ring',1973,2)
    ]