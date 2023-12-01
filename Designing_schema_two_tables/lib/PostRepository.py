from lib.Post import Post
from lib.Comment import Comment
class PostRepository:
    def __init__(self,connection):
        self._connection = connection
    def post_with_comments(self,post_number):
        return_data = []
        comments =[]
        rows = self._connection.execute(
            '''
            SELECT 
                posts.id as post_id,
                posts.title as post_title,
                posts.content as post_content,
                comments.id as comment_id,
                comments.author_name,
                comments.content as comment_content,
                comments.posts_id
            FROM posts
            JOIN comments
            ON posts.id = comments.posts_id
            WHERE posts.id = %s
            ''',[post_number]
        )
        data = Post(rows[0]['post_id'],rows[0]['post_title'],rows[0]['post_content'])
        return_data.append(data)

        for row in rows:
            data = Comment(row['comment_id'],row['author_name'],row['comment_content'],row['posts_id'])
            comments.append(data)
        return_data.append(comments)
        return return_data