from UI import Ui
from SERVICES import Manage_school
from REPOSITORY import School_repository

def Start_Program():
    repository = School_repository()

    repository.generateStudentsRepository()
    repository.generateDisciplineRepository()
    repository.generateGradeRepository()

    manager = Manage_school(repository)
    ui = Ui(manager)
    ui.start()

if __name__ == '__main__':
    Start_Program()
