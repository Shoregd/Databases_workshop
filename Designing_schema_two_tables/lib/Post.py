class Post:
    def __init__(self,id,title,content):
        self.id = id
        self.title = title
        self.content = content
    def __repr__(self):
        return f'Post({self.id}, {self.title}, {self.content})'
    def __eq__(self,other):
        return self.__dict__ == other.__dict__