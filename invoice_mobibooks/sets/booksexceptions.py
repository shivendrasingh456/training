#invoice book exception
class BooksException(Exception):
    def __init__(self,code,message):
        self.code = code
        self.message = message
