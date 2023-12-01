from lib.Tag import Tag
from lib.Post import Post

class TagRepository:
    def __init__(self,connection):
        self._connection = connection
    def find_by_post(self,post_number):
        rows = self._connection.execute(
            '''SELECT
            tags.id as tags_id,
            tags.name as tag_name
           FROM tags
           JOIN posts_tags ON posts_tags.tag_id = tags.id
           JOIN posts ON posts_tags.post_id = posts.id
           WHERE posts.id = %s
           ''',[post_number]
        )
        return_data = []
        for row in rows:
            data = Tag(row['tags_id'],row['tag_name'])
            return_data.append(data)

        return return_data