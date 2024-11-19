from src.DOMAIN import Student

class StudentRepository:
    def __init__(self,file_name:str):
        """
        Here we have repository class where we cant Take and put informations in files
        students_repository is the repository which we work with to do all assignements
        :param file_name:
        """
        self.students_repository = []
        self.file_name = file_name

    def take_from_file(self):
        """
        here we have the function witch help us to take informations from file
        :return: students_repository with all assignements in it
        """
        self.students_repository.clear()

        with open(self.file_name,"r") as file:
            datas = file.read()

            if datas:
                lines = datas.split("\n")

                for line in lines:
                    if len(line) > 1:
                        id,name,solution = line.split(",")
                        self.students_repository.append(Student(int(id), str(name), str(solution)))


    def put_in_file(self):
        """
        Here we have the function wich help us to store modified informations from students_repository in file
        :return: A fresh Students_repo with updated informations
        """
        with open(self.file_name,"w") as file:
            for student in self.students_repository:
                file.write(f"{student.get_id()},{student.get_name()},{student.get_solution()}\n")