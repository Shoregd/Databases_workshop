from lib.album import Album

class AlbumsRepository:
    #Initialise class with database connection.
    def __init__(self,connection):
        self._connection = connection

    #Create method that lists all albums held in the database.
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            data = Album(row['id'],row['title'],row['release_year'],row['artist_id'])
            albums.append(data)
        return albums