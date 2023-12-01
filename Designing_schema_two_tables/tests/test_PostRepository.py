from lib.Post import Post
from lib.Comment import Comment
from lib.PostRepository import PostRepository

def test_repository_returns_post_and_comments(db_connection):
    db_connection.seed('seeds/blog_setup.sql')
    repository = PostRepository(db_connection)
    result = repository.post_with_comments(1)
    assert result ==[
                Post(1,'Test Title','This is some test content.'),
                [
                    Comment(1,'Terry','Test comment',1),
                    Comment(2,'Greg','Test comment',1),
                    Comment(3,'Paul','Test comment',1)
                ]
            ]
