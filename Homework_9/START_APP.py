from SETINGS_PROPERTIES import Setings
from SERVICES import Manage_school
from UI import Ui


def start_application():
    TEXT_REPOSITORY = 1
    BINATY_REPOSITORY = 2
    EXIT = 3

    while True:
        print("1. Text repository")
        print("2. Binary repository")
        print("3. Exit")

        command = int(input("Input your choice: "))

        if command == TEXT_REPOSITORY:

            repository = Setings(TEXT_REPOSITORY)
            manage = Manage_school(repository)
            ui = Ui(manage)
            ui.start()

        elif command == BINATY_REPOSITORY:

            repository = Setings(BINATY_REPOSITORY)
            manage = Manage_school(repository)
            ui = Ui(manage)
            ui.start()

        elif command == EXIT:
            print("Exiting")
            break
        else:
            print("Invalid command")



if __name__ == "__main__":
    start_application()