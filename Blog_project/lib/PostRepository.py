from lib.Post import Post
from lib.Tag import Tag

class PostRepository:
    def __init__(self,connection):
        self._connection = connection
    def find_by_tag(self,tag_name):
        rows = self._connection.execute(
            '''SELECT
            posts.id as posts_id,
            posts.title as post_title
           FROM posts
           JOIN posts_tags ON posts_tags.post_id = posts.id
           JOIN tags ON posts_tags.tag_id = tags.id
           WHERE tags.name = %s
           ''',[tag_name] 
        )
        return_data = []
        for row in rows:
            data = Post(row['posts_id'],row['post_title'])
            return_data.append(data)
        
        return return_data
        