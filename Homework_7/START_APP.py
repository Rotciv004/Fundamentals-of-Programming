from REPOSITORY import Binary_Repository,File_Repository
from SERVICES import ManageBooks
from UI import Ui
def start_app():
    TEXT = 1
    BINARY =2
    EXIT =3

    print("Welcome to the aplication choose your repository")
    print("1. Text repository")
    print("2. Binary repository")
    print("3. Exit")

    command = int(input("Enter your choice: "))

    while True:
        if command == TEXT:
            repository = File_Repository("BOOKS_TEXT.txt")
            manage = ManageBooks(repository)
            ui = Ui(manage)
            ui.start()


        elif command == BINARY:
            repository = Binary_Repository("BOOKS_BINARY.txt")
            manage = ManageBooks(repository)
            ui = Ui(manage)
            ui.start()

        elif command == EXIT:
            print("Exit")
            break
        else:
            print("Invalid choice")

        break

if __name__ == "__main__":
    start_app()