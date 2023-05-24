class Book:
    def __init__(self, id=0, publisher_id=None, book_name=None, year=0, price=0):
        self.id = id
        self.publisher_id = publisher_id
        self.book_name = book_name
        self.year = year
        self.price = price


class Publisher:
    def __init__(self, id=0, name=None):
        self.id=id
        self.name=name
    
