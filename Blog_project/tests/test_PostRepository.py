from lib.PostRepository import PostRepository
from lib.Post import Post
from lib.Tag import Tag

def test_find_by_tag_returns_list_of_posts(db_connection):
    db_connection.seed('seeds/blog_project.sql')
    repository = PostRepository(db_connection)
    result = repository.find_by_tag('coding')
    assert result == [
        Post(1,'How to use Git'),
        Post(2,'Fun classes'),
        Post(3,'Using a REPL'),
        Post(7,'SQL basics')
    ]