class Comment:
    def __init__(self,id,author_name,content,post_id):
        self.id = id
        self.author_name = author_name
        self.content = content
        self.post_id = post_id
    def __repr__(self):
        return f'Comment({self.id}, {self.author_name}, {self.content}, {self.post_id})'
    def __eq__(self,other):
        return self.__dict__ == other.__dict__