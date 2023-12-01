from lib.TagRepository import TagRepository
from lib.Post import Post
from lib.Tag import Tag

def test_find_by_post_returns_list_of_tags(db_connection):
    db_connection.seed('seeds/blog_project.sql')
    repository = TagRepository(db_connection)
    result = repository.find_by_post(2)
    assert result ==[
                    Tag(1,'coding'),
                    Tag(4,'education')
    ]