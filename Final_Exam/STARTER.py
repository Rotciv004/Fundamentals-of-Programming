from BOARD import Board
from SERVICES import Service
from UI import Ui

services = Service(Board)
ui = Ui(services)

if __name__ == "__main__":
    ui.menu()