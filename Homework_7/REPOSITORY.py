from DOMAIN import Book
import pickle

class File_Repository:
    def __init__(self,file_name):
        self.books = []
        self.books_repo = []
        self.file_name = file_name

    def load_data(self):
        self.books.clear()

        with open(self.file_name, 'r') as file:
            data = file.read()

            if data:
                lines = data.split('\n')

                for line in lines:
                    if len(line) > 0:
                        isbn, author, title = line.split(",")
                        self.books.append(Book(int(isbn), author, title))

    def save_data(self):
        with open(self.file_name, 'w') as file:
            for book in self.books:
                file.write(f"{book.get_isbn()},{book.get_author()},{book.get_title()}\n")

class Binary_Repository:
    def __init__(self,file_name):
        self.books = []
        self.books_repo = []
        self.file_name = file_name

    def load_data(self):
        self.books.clear()

        with open(self.file_name, 'rb') as file:
            data = file.read()

            if data:
                self.books = pickle.loads(data)

    def save_data(self):
        with open(self.file_name, 'wb') as file:
            file.write(pickle.dumps(self.books))
