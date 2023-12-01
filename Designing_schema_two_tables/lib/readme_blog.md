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
 * post_id: token from posts

--- RELATIONSHIPS --- 

Posts can have many comments. Comments belong to posts. Comments has the foreign key.

--- CLASS SETUP ---

 * Post - Model Class
    * __init__: id,title,content
    * __repr__: returns 'Post(id,title,content)
    * __eq__: Allows for testing

* Comment - Model Class
    * __init__: id,author_name,content, posts_id
    * __repr__: returns 'Comment(id,author_name,content,posts_id)
    * __eq__: Allows for testing

* PostRepository - Repository Class
    * __init__: establishes database connection only using fed db_connection
    * post_with_comments(post_number:int): will return a list containing the post and a list of comments associated with that post.
    I.e post_with_comments(1) would return [Post(1,'Test Title', 'This is some test content.'),[Comment(1,'Terry','Test comment',1),Comment(2,'Greg','Test comment',1),Comment(3,'Paul','Test comment',1)]]
    executing 
    '''
    SELECT 
        posts.id as post_id,
        posts.title as post_title,
        posts.content as post_content,
        comments.id as comment_id,
        comments.author_name,
        comments.content as comment_content
        comments.posts_id as posts_id
    FROM posts
    JOIN comments
    ON posts.id = comments.posts_id
    WHERE posts.id = %s
    ''', [post_number]