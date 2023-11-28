As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.

--- NOUNS ---

 * post, title, content, comment, author_name


--- TABLE LAYOUT ---

Posts:

RECORD | PROPERTIES

post   | id,title,content

Comments:

RECORD | PROPERTIES

comment | id, author_name, content

--- DATA TYPES ---

Posts:
 * id:serial
 * title: text
 * content: text

Comments:
 * id:serial
 * author_name: text
 * content: text

--- RELATIONSHIPS --- 

Posts can have many comments. Comments belong to posts. Comments has the foreign key.