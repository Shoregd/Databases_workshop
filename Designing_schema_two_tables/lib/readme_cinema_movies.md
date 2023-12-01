As a cinema company manager,
So I can keep track of movies being shown,
I want to keep a list of movies with their title and release date.

As a cinema company manager,
So I can keep track of movies being shown,
I want to keep a list of my cinemas with their city name (e.g 'London' or 'Manchester').

As a cinema company manager,
So I can keep track of movies being shown,
I want to be able to list which cinemas are showing a specific movie.

As a cinema company manager,
So I can keep track of movies being shown,
I want to be able to list which movies are being shown a specific cinema.

--- NOUNS ---

movies, title, release_date, cinemas, city_name

--- TABLE LAYOUT ---

RECORD  | PROPERTIES

Movies | id,title,release_date

Cinemas | id,city_name

--- DATA TYPES ---

Movies:
    * id: SERIAL
    * title: text
    * release_date: date

Cinemas:
    * id: SERIAL
    * city_name: text

--- RELATIONSHIPS ---

Cinemas can have MANY movies. Movies can play in MANY cinemas.
Join table needed.

--- JOIN TABLE LAYOUT ---

Join table for tables: Movies and cinemas
Join table name: movies_cinemas
Columns: movie_id, cinema_id

