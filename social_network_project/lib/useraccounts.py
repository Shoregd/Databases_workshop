from lib.Post import Post
from lib.useraccount import UserAccount

class UserAccounts:
    def __init__(self,connection):
        self._connection = connection

    def all_users(self):
        rows = self._connection.execute('Select * from user_accounts')
        users = []
        for row in rows:
            data = UserAccount(row['id'],row['username'],row['email_address'])
            users.append(data)
        return users
    def posts_by_user(self,user_id):
        rows = self._connection.execute('Select * from posts WHERE useraccount_id = %s',[user_id])
        posts = []
        for row in rows:
            data = Post(row['id'],row['title'],row['content'],row['views'],row['useraccount_id'])
            posts.append(data)
        return posts
    def post_by_user(self,user_id,post_id):
        rows = self._connection.execute('SELECT * FROM posts WHERE (useraccount_id = %s AND id = %s)',[user_id,post_id])
        row = rows[0]
        return Post(row['id'],row['title'],row['content'],row['views'],row['useraccount_id'])
    def create_user(self,user_name,email_add):
        self._connection.execute(
            'INSERT INTO user_accounts (username,email_address) VALUES(%s,%s)',[user_name,email_add]
        )
    def create_post(self,user_id,post_title,post_contents,post_views):
        self._connection.execute(
            'INSERT INTO posts (title,content,views,useraccount_id) VALUES(%s,%s,%s,%s)',[post_title,post_contents,post_views,user_id]
        )