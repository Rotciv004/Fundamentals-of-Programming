from DOMAIN import Student,Grade,Discipline
class Manage_school:
    def __init__(self,repository):
        self.repository = repository

    def add_a_student(self,student:Student) -> bool:
        for stud in self.repository.students_repository:
            if student.get_id() == stud.get_id():
                return False

        self.repository.students_repository.append(student)

        return True
    def delete_a_student(self,student_id:int)->bool:
        VALIDATION = False

        for student in self.repository.students_repository:
            if student.get_id() == student_id:
                self.repository.students_repository.remove(student)
                VALIDATION = True

        if VALIDATION:
            for grade in self.repository.grades_repository:
                if student_id == grade.get_student_id():
                    self.repository.grades_repository.remove(grade)

        return VALIDATION

    def list_all_students(self) -> list:
        return self.repository.students_repository
    def update_a_student(self, update_student:Student)->bool:
        for student in self.repository.students_repository:
            if student.get_id() == update_student.get_id():
                student.set_name(update_student.get_name())
                return True

        return False

    def search_after_a_student_by_id(self, student_id:int) -> Student:
        for student in self.repository.students_repository:
            if student.get_id() == student_id:
                return student

    def search_after_a_student_by_name(self, student_name:str)->list:
        students_list = []

        for student in self.repository.students_repository:
            if student_name.lower() in student.get_name().lower():
                students_list.append(student)

        return students_list
    def add_a_grade(self, grade:Grade)->bool:
        for student in self.repository.students_repository:
            if student.get_id() == grade.get_student_id():
                for discipline in self.repository.disciplines_repository:
                    if discipline.get_id() == grade.get_discipline_id():
                        if grade.get_value() >= 0 and grade.get_value() <= 10:
                            self.repository.grades_repository.append(grade)
                            return True

        return False




    def list_all_grades_for_a_student(self,student_id:int)->list:
        grades_list = []

        for grade in self.repository.grades_repository:
            if grade.get_student_id() == student_id:
                grades_list.append(grade)

        return grades_list

    def list_all_grades(self)-> list:
        return self.repository.grades_repository


    def add_a_discipline(self, discipline:Discipline)-> bool:
        for dis in self.repository.disciplines_repository:
            if dis.get_id() == discipline.get_id() or dis.get_name() == discipline.get_name():
                return False

        self.repository.disciplines_repository.append(discipline)

        return True

    def delete_a_discipline(self,discipline_id:int)->bool:
        VALIDATION = False
        for discipline in self.repository.disciplines_repository:
            if discipline.get_id() == discipline_id:
                self.repository.disciplines_repository.remove(discipline)
                VALIDATION = True

        for grade in self.repository.grades_repository:
            if discipline_id == grade.get_discipline_id():
                self.repository.grades_repository.remove(grade)

        return VALIDATION

    def list_all_disciplines(self)->list:
        return self.repository.disciplines_repository

    def update_a_discipline(self,updated_discipline:Discipline)->bool:
        for discipline in self.repository.disciplines_repository:
            if discipline.get_id() == updated_discipline.id:
                discipline.set_name(updated_discipline.get_name())
                return True

        return False

    def search_after_a_discipline_by_id(self,discipline_id:int) -> Discipline:
        for discipline in self.repository.disciplines_repository:
            if discipline.get_id() == discipline_id:
                return discipline

    def search_after_a_discipline_by_name(self,discipline_name:str):
        disciplines_list = []

        for discipline in self.repository.disciplines_repository:
            if discipline_name.lower() in discipline.get_name().lower():
                disciplines_list.append(discipline)

        return disciplines_list

    def failing_students(self)->list:
        failing_students = []

        for student in self.repository.students_repository:
            for discipline in self.repository.disciplines_repository:
                student_grades = []

                for grade in self.repository.grades_repository:
                    if grade.get_student_id() == student.get_id() and grade.get_discipline_id() == discipline.get_id():
                        student_grades.append(grade.get_value())

                if student_grades:
                    average_grade = sum(student_grades) / len(student_grades)
                    if average_grade < 5:
                        failing_students.append(student)
                        break

        return failing_students

    def best_students(self) -> list:
        best_students = []
        average_grade_student = []

        for student in self.repository.students_repository:
            student_grades = []

            for grade in self.repository.grades_repository:
                if grade.get_student_id() == student.get_id():
                    student_grades.append(grade.get_value())

            if student_grades:
                average_grade = sum(student_grades) / len(student_grades)
                if average_grade >= 5:
                    best_students.append(student)
                    average_grade_student.append(average_grade)

        best_students, average_grade_student = zip(
            *sorted(zip(best_students, average_grade_student), key=lambda x: x[1], reverse=True))

        return best_students

    def disciplines_with_at_least_one_grade(self)->list:
        discipline_list = []

        for discipline in self.repository.disciplines_repository:
            for grade in self.repository.grades_repository:
                if grade.get_discipline_id() == discipline.get_id():
                    discipline_list.append(discipline)
                    break

        return discipline_list


    def give_a_grade_to_a_student(self,grade_to_add:Grade)->bool:
        VALIDATION = True

        if grade_to_add.get_value() < 0 or grade_to_add.get_value() > 10:
            VALIDATION = False

        if VALIDATION:
            VALIDATION = False

            for student in self.repository.students_repository:
                if student.get_id() == grade_to_add.get_student_id():
                    VALIDATION = True
                    break

        if VALIDATION:
            VALIDATION = False

            for discipline in self.repository.disciplines_repository:
                if discipline.get_id() == grade_to_add.get_discipline_id():
                    VALIDATION = True
                    break

        if VALIDATION:
            self.repository.grades_repository.append(grade_to_add)
            return True
        else:
            return False
