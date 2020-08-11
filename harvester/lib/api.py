class API():
    def __init__(self, title, publisher):
        self.title = title
        self.publisher = publisher

    def serialize(self):
        return {
            'title': self.title,
            'publisher': self.publisher,
        }
