class Album:
    #Initialise class with base attributes from the seeded table.
    #Attributes will be id, title, release_year, artist_id default is none
    def __init__(self,id,title,release_year,artist_id=None):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id=artist_id
    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})'

