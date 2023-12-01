Method |	Job	Arguments | 	SQL query | 	Returns
find_by_tag	| Find all posts for the given tag |	A tag (string)|	SELECT ... JOIN  |	Array of Post

--- INFERRED NOUNS ---

posts, title, tags, name

--- TABLE LAYOUT ---

RECORD | PROPERTIES

posts | id,title

tags | id,name

--- DATA TYPES ---

Posts:
    * id:SERIAL
    * title: text

Tags:
    * id:SERIAL
    * name: text

--- RELATIONSHIPS ---

A post can have MANY tags. A tag can be in MANY posts.
Requires join table.

--- JOIN TABLE LAYOUT ---

Join table tables: Posts, Tags
Join table name: posts_tags
Columns: post_id,tag_id

SQL located in blog_project.sql
tables created in blog_project_db

--- CLASS BREAKDOWN ---

Post - Model Class
    * __init__: id,title
    * __repr__: Post(id,title)
    * __eq__: Allows for testing

Tag - Model Class
    * __init__: id,name
    * __repr__: Tag(id,name)
    * __eq__: Allow for testing

PostRepository - Repository class
    * __init__: databaseconnection taking connection as input. Returns nothing
    * find_by_tag(): returns list of post objects that have the associated tag name. Input tag_name: string returns List of objects. No other side effects.
        executes
        '''SELECT
            posts.id as posts_id
            posts.title as post_title
           FROM posts
           JOIN posts_tags ON posts_tags.post_id = posts.id
           JOIN tags ON posts_tags.tag_id = tags.id
           WHERE tags.name = %s
           ''',[tag_name] 

    I.E find_by_tag('coding') would return [Post(1,'How to use Git'),Post(2,'Fun Classes'),Post(3,'Using a REPL'),Post(7,'SQL basics')]


--- CHALLENGE ADDITIONS ---
Wants implementation of TagRepository with method find_by_post accepts a post ID returns list of tag names associated

--- CLASS BREAKDOWN ---
Re-using Post and Tag from above as model classes

TagRepository - Repository Class
    * __init__: databaseconnection taking connection as input. returns nothing
    * find_by_post(): returns list of tag objects assiciated with the supplied post_id. Input post_number: int returns list of objects. no other side effects.
        executes
        '''
        '''SELECT
            tags.id as tags_id,
            tags.name as tag_name
           FROM tags
           JOIN posts_tags ON posts_tags.tag_id = tags.id
           JOIN posts ON posts_tags.post_id = posts.id
           WHERE posts.id = %s
           ''',[post_number]