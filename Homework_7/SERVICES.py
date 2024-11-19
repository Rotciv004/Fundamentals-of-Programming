from DOMAIN import Book
import copy

class ManageBooks():
    def __init__(self,repository):
        self.repository = repository

    def add_a_book(self, book: Book)->bool:
        self.repository.load_data()

        self.repository.books_repo.append(copy.deepcopy(self.repository.books))


        for boo in self.repository.books:
            if boo.get_isbn() == book.get_isbn():
                return False

        self.repository.books.append(book)

        self.repository.save_data()

        return True

    def display_the_list_of_books(self)->list:
        self.repository.load_data()

        return self.repository.books

    def filter_the_list(self, key_word: str)->list:
        self.repository.load_data()

        filtered_books = []

        for book in self.repository.books:
            if book.title.lower().startswith(key_word.lower()):
                filtered_books.append(book)

        return filtered_books

    def undo(self)->bool:
        if self.repository.books_repo:
            self.books = self.repository.books_repo.pop()
        else:
            return False

        self.repository.save_data()

        return True

