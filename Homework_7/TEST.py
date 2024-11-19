import unittest
from REPOSITORY import Binary_Repository,File_Repository
from SERVICES import ManageBooks
from DOMAIN import Book

class TestManageBooks_file(unittest.TestCase):
    def setUp(self):
        self.repository = File_Repository("BOOKS_TEXT.txt")
        self.manage = ManageBooks(self.repository)

    def test_add_a_book(self):
        self.repository.load_data()

        initial_len = len(self.repository.books)
        self.manage.add_a_book(Book(999999,"MANSDADAD","qdqdqdqdqd"))

        self.assertEqual(len(self.repository.books),initial_len+1)


    def test_display_the_list_of_books(self):
        self.repository.load_data()

        initial_len = len(self.repository.books)

        self.assertEqual(len(self.manage.display_the_list_of_books()),initial_len)

    def test_filter_the_list(self):
        self.repository.load_data()

        self.manage.add_a_book(Book(99999999,"a","a"))
        self.assertTrue(len(self.manage.filter_the_list("a")) >= 1)



class TestManageBooks_binary(unittest.TestCase):
    def setUp(self):
        self.repository = Binary_Repository("BOOKS_BINARY.txt")
        self.manage = ManageBooks(self.repository)

    def test_add_a_book(self):
        self.repository.load_data()

        initial_len = len(self.repository.books)
        self.manage.add_a_book(Book(999999,"MANSDADAD","qdqdqdqdqd"))

        self.assertEqual(len(self.repository.books),initial_len+1)


    def test_display_the_list_of_books(self):
        self.repository.load_data()

        initial_len = len(self.repository.books)

        self.assertEqual(len(self.manage.display_the_list_of_books()),initial_len)

    def test_filter_the_list(self):
        self.repository.load_data()

        self.manage.add_a_book(Book(99999999,"a","a"))
        self.assertTrue(len(self.manage.filter_the_list("a")) >= 1)






