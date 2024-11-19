from src.REPOSITORY import StudentRepository
from src.SERVICES import Services
from src.UI import Ui

def start_aplication():
    """
    Here we have the function witch starts the program
    :return: Start the entire program
    """
    repository_name = "Students_repo.txt"
    repository = StudentRepository(repository_name)
    services = Services(repository)
    ui = Ui(services)
    ui.menu()

if __name__ == "__main__":
    start_aplication()
