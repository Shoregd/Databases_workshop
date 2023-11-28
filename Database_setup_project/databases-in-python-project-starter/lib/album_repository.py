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
    
    #Create a method to find a single record based on provided id.
    def find(self,album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s',[album_id]
        )
        row = rows[0]
        return Album(row['id'],row['title'],row['release_year'],row['artist_id'])
    
    def add_album(self,art_id,album_title,release_yr):
        self._connection.execute(
            'INSERT INTO albums (title,release_year,artist_id) VALUES(%s,%s,%s)', [album_title,release_yr,art_id]
        )
    def delete_album(self,album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [album_id]
        )