from DOMAIN import Student,Discipline,Grade
import pickle

class Text_File_Repo:
    def __init__(self,file_name_students:str,file_name_disciplines:str,file_name_grades:str):
        self.file_name_students = file_name_students
        self.file_name_disciplines = file_name_disciplines
        self.file_name_grades = file_name_grades
        self.students_repository= []
        self.grades_repository = []
        self.disciplines_repository = []

    def take_from_files(self):
        self.students_repository.clear()
        self.disciplines_repository.clear()
        self.grades_repository.clear()

        with open(self.file_name_students,'r') as file:
            datas = file.read()

            if datas:
                lines = datas.split('\n')
                for line in lines:
                    if len(line) > 2:
                        id,name = line.split(",")
                        self.students_repository.append(Student(int(id), name))


        with open(self.file_name_disciplines,'r') as file:
            datas = file.read()

            if datas:
                lines = datas.split('\n')
                for line in lines:
                    if len(line) > 2:
                        id,name = line.split(",")
                        self.disciplines_repository.append(Discipline(int(id), name))


        with open(self.file_name_grades,'r') as file:
            datas = file.read()

            if datas:
                lines = datas.split('\n')
                for line in lines:
                    if len(line) > 3:
                        student_id,disiciplin_id,value = line.split(",")
                        self.grades_repository.append(Grade(int(student_id), int(disiciplin_id), float(value)))

    def put_in_files(self):
        with open(self.file_name_students,'w') as file:
            for student in self.students_repository:
                file.write(f"{student.get_id()},{student.get_name()}\n")

        with open(self.file_name_disciplines,'w') as file:
            for disciplin in self.disciplines_repository:
                file.write(f"{disciplin.get_id()},{disciplin.get_name()}\n")


        with open(self.file_name_grades,'w') as file:
            for grade in self.grades_repository:
                file.write(f"{grade.get_student_id()},{grade.get_discipline_id()},{grade.get_value()}\n")



class Binary_File_Repo:
    def __init__(self,file_name_students:str,file_name_disciplines:str,file_name_grades:str):
        self.file_name_students = file_name_students
        self.file_name_disciplines = file_name_disciplines
        self.file_name_grades = file_name_grades
        self.students_repository = []
        self.grades_repository = []
        self.disciplines_repository = []

    def take_from_files(self):
        self.students_repository.clear()
        self.grades_repository.clear()
        self.disciplines_repository.clear()

        with open(self.file_name_students, 'rb') as file:
            data = file.read()

            if data:
                self.students_repository = pickle.loads(data)

        with open(self.file_name_grades, 'rb') as file:
            data = file.read()

            if data:
                self.grades_repository = pickle.loads(data)

        with open(self.file_name_disciplines, 'rb') as file:
            data = file.read()

            if data:
                self.disciplines_repository = pickle.loads(data)

    def put_in_files(self):
        with open(self.file_name_students, 'wb') as file:
            file.write(pickle.dumps(self.students_repository))

        with open(self.file_name_grades, 'wb') as file:
            file.write(pickle.dumps(self.grades_repository))

        with open(self.file_name_disciplines, 'wb') as file:
            file.write(pickle.dumps(self.disciplines_repository))



