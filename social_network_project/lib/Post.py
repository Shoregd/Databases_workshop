class Post:
    def __init__(self,id,title,contents,views,useraccount_id):
        self.id  = id
        self.title = title
        self.contents = contents
        self.views = views
        self.useraccount_id = useraccount_id

    def __repr__(self):
        return f'Post({self.id}, {self.title}, {self.contents}, {self.views}, {self.useraccount_id})'
    
    def __eq__(self,other):
        return self.__dict__ == other.__dict__