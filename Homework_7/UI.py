from DOMAIN import Book

class Ui():

    def __init__(self,manage):
        self.manage = manage

    def get_command(self,message:str)->int:
        return int(input(f"{message} --> "))

    def get_isbn(self,message:str)->int:
        return int(input(f"{message} --> "))

    def get_title(self,message:str)->str:
        return str(input(f"{message} --> "))

    def get_author(self,message:str)->str:
        return str(input(f"{message} --> "))

    def start(self):
        ADD_A_BOOK = 1
        DISPALY_ALL_BOOKS = 2
        FILTER_THE_LIST = 3
        UNDO = 4
        EXIT = 5

        while True:
            print("1. Add a book")
            print("2. Display all books")
            print("3. Filter the list of book after a key word")
            print("4. Undo")
            print("5. Exit")

            command = self.get_command("Input command")

            if command == ADD_A_BOOK:
                isbn = self.get_isbn("Input isbn")
                author = self.get_author("Input author")
                title = self.get_title("Input title")

                if self.manage.add_a_book(Book(isbn,author,title)):
                    print("Book added successfully")
                else:
                    print("Invalid input")

            elif command == DISPALY_ALL_BOOKS:
                list_of_books = self.manage.display_the_list_of_books()

                if list_of_books:
                    for book in list_of_books:
                        print(book)
                else:
                    print("No books found")

            elif command == FILTER_THE_LIST:
                key_word = str(input("Input the key word --> "))

                list_of_books = self.manage.filter_the_list(key_word)

                if list_of_books:
                    for book in list_of_books:
                        print(book)
                else:
                    print("No books found")

            elif command == UNDO:
                if self.manage.undo():
                    print("Undoing")
                else:
                    print("No undo steps")

            elif command == EXIT:
                print("Exiting")
                break

            else:

                print("Invalid input")



