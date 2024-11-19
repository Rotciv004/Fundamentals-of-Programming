class Book:
    def __init__(self, isbn: int, author: str, title: str):
        self.isbn = isbn
        self.author = author
        self.title = title

    def get_isbn(self)->int:
        return self.isbn

    def set_isbn(self, isbn:int):
        self.isbn = isbn

    def get_author(self)->str:
        return self.author

    def set_author(self, author:str):
        self.author=author

    def get_title(self)->str:
        return self.title

    def set_title(self, title:str):
        self.title = title

    def __str__(self):
        return (f"{self.isbn} - {self.author} - {self.title}")
