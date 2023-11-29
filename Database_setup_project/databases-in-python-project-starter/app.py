# file: app.py

from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection
from lib.album_repository import AlbumsRepository

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!
    print('Welcome to the music library manager!\n\n')
    print('What would you like to do?')
    print('1 - List all albums')
    print('2 - List all artists\n')

    
    choice = int(input('Enter your choice: '))
    print('\n\n\n')
    if choice ==1:
       album_repository = AlbumsRepository(self._connection)
       albums = album_repository.all()
       print('Here is a list of albums:')
       for album in albums:
          print(f'  * {album.id} - {album.title}')
    elif choice == 2:

        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()
        print('Here is a list of artists:')
        for artist in artists:
            print(f"  * {artist.id}: {artist.name} ({artist.genre})")

if __name__ == '__main__':
    app = Application()
    app.run()