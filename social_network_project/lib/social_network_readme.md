As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

--- NOUNS ---

 * user_account, email_address, username, posts, title, content, views

--- TABLE LAYOUT --- 

User_accounts:

RECORD | PROPERTIES

user_account | id,username,email_address

Posts:

RECORD | PROPERTIES

post   | id,title,content,views


--- DATA TYPES ---

User_accounts:
 * id: serial
 * username: text
 * email_address: text

Posts:
 * id: serial
 * title: text
 * content: text
 * views: int

--- RELATIONSHIPS --- 

User account can have many posts. Posts belong to user account. Posts will have the foreign key linked to user account.

--- CLASS STRUCTURES ---

* UserAccounts - Repository
    * will hold a list of UserAccount classes
    * all_users() will list all user accounts using 'SELECT * FROM User_accounts'
    * posts_by_user(account_id) will list all posts by the specified user 
        'SELECT * FROM posts WHERE useraccount_id = %s', [account_id]
    * post_by_user(account_id,post_id) will list a single post by the specified user 
    'SELECT * FROM posts WHERE (useraccount_id = %s AND id = %s)',[account_id,post_id]
    * create_user(user_name,email_add) will create a new user with the specified username and email_address then return the created UserAccount class
    'INSERT INTO user_accounts (username,email_address) VALUES(user_name,email_add)'
    * create_post(user,post_title,post_content,post_views) will create a new post for the specified user
    'INSERT INTO posts (title,content,views,useraccount_id) VALUES(post_title,post_content,post_views,user)'

* UserAccount - Model
    * __init__: id, username, email_address
    * __repr__: UserAccount(id, username, email_address)
    * __eq__: To enable class testing

* Post - Model
    * __init__: id,title,content,views,useraccount_id
    * __repr__: Post(id, title, content, views, useraccount_id)
    * __eq__: To enable class testing