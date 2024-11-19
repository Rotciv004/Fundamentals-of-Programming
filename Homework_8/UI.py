from DOMAIN import Student, Discipline,Grade
class Ui:
    def __init__(self,services):
        self.services = services

    def get_command(self,message:str)->int:
        return int(input(message))
    def print_message(self,message:str):
        print(message)
    def get_id(self,message:str)->int:
        return int(input(message))
    def get_name(self,message:str)->str:
        return str(input(message))
    def get_grade_value(self,message:str)->float:
        return float(input(message))
    def display_error(self,error_text:str):
        print(f"Error: {error_text}")

    def start(self):

        ADD_A_STUDENT = 1
        DELETE_A_STUDENT = 2
        LIST_ALL_STUDENTS = 3
        UPDATE_A_STUDENT = 4
        ADD_A_DISCIPLINE = 5
        DELETE_A_DISCIPLINE = 6
        LIST_ALL_DISCIPLINE = 7
        UPDATE_A_DISCIPLINE = 8
        GIVE_A_GRADE_TO_A_STUDENT = 9
        SEARCH_FOR_A_STUDENT = 10
        SEARCH_FOR_A_DISCIPLINE = 11
        FAILING_STUDENTS = 12
        BEST_STUDENTS = 13
        LIST_ALL_DISCIPLINES_WITH_AT_LEAST_ONE_GRADE = 14
        DISPLAY_ALL_GRADES_FOR_A_STUDENT = 15
        DISPLAY_ALL_GRADES = 16
        EXIT = 17

        while True:
            print("1. Add a student")
            print("2. Delet a student")
            print("3. List all students")
            print("4. Update a student")
            print("5. Add a discipline")
            print("6. Delet a discipline")
            print("7. List all disciplines")
            print("8. Update a discipline")
            print("9. Give a grade to a student")
            print("10. Search for a student")
            print("11. Search for a discipline")
            print("12. Failing students")
            print("13. Best students")
            print("14. List all disciplines with at least one grade")
            print("15. Display all grades for a student")
            print("16. Display all grades")
            print("17. Exit")

            command = self.get_command("Input command --> ")

            if command == ADD_A_STUDENT:
                id = self.get_id("Input student id --> ")
                name = self.get_name("Input student name --> ")

                if self.services.add_a_student(Student(id, name)):
                    self.print_message("Student added successfully")

                else:
                    self.display_error("Invalid input value")

            elif command == DELETE_A_STUDENT:
                id = self.get_id("Input student id --> ")

                if self.services.delete_a_student(id):
                    self.print_message("Student deleted successfully")
                else:
                    self.display_error("Invalid input value")

            elif command == LIST_ALL_STUDENTS:
                student_list = self.services.list_all_students()

                if student_list:
                    for student in student_list:
                        print(student)
                else:
                    self.print_message("Empty list")

            elif command == UPDATE_A_STUDENT:
                id = self.get_id("Input student id --> ")
                name = self.get_name("Input student new name --> ")

                if self.services.update_a_student(Student(id, name)):
                    self.print_message("Student updated successfully")
                else:
                    self.display_error("Invalid input value")

            elif command == ADD_A_DISCIPLINE:
                id = self.get_id("Input discipline id --> ")
                name = self.get_name("Input discipline new name --> ")

                if self.services.add_a_discipline(Discipline(id, name)):
                    self.print_message("Discipline added successfully")
                else:
                    self.display_error("Discipline already exists")

            elif command == DELETE_A_DISCIPLINE:
                id = self.get_id("Input discipline id --> ")

                if self.services.delete_a_discipline(id):
                    self.print_message("Discipline deleted with succes")
                else:
                    self.display_error("Discipline does not exist")

            elif command == LIST_ALL_DISCIPLINE:
                discipline_list = self.services.list_all_disciplines()

                if discipline_list:
                    for discipline in discipline_list:
                        print(discipline)
                else:
                    self.print_message("Empty list")

            elif command == UPDATE_A_DISCIPLINE:
                id = self.get_id("Input discipline id --> ")
                name = self.get_name("Input discipline new name --> ")

                if self.services.update_a_discipline(Discipline(id, name)):
                    self.print_message("Discipline updated successfully")
                else:
                    self.display_error("Discipline does not exist")

            elif command == GIVE_A_GRADE_TO_A_STUDENT:
                student_id = self.get_id("Input student id --> ")
                discipline_id = self.get_id("Input discipline id --> ")
                grade_value = self.get_grade_value("Input grade value --> ")

                if self.services.give_a_grade_to_a_student(Grade(student_id, discipline_id, grade_value)):
                    self.print_message("Grade updated successfully")
                else:
                    self.display_error("Invalid input datas")

            elif command == SEARCH_FOR_A_STUDENT:
                BY_ID = 1
                BY_NAME = 2

                print("1. Search by id")
                print("2. Search by name")

                command = self.get_command("Input command --> ")

                if command == BY_ID:
                    id = self.get_id("Input id for student --> ")

                    if self.services.search_after_a_student_by_id(id):
                        print(self.services.search_after_a_student_by_id(id))
                    else:
                        self.display_error("We do not have this student")

                elif command == BY_NAME:
                    name = self.get_name("Input name for student --> ")
                    students_list = self.services.search_after_a_student_by_name(name)

                    if students_list:
                        for student in students_list:
                            print(student)
                    else:
                        self.display_error("We do not have a student")
                else:
                    self.print_message("Invalid command")

            elif command == FAILING_STUDENTS:
                failing_students_list = self.services.failing_students()

                if failing_students_list:
                    for student in failing_students_list:
                        print(student)
                else:
                    self.print_message("Empty list")

            elif command == BEST_STUDENTS:
                best_students_list = self.services.best_students()

                if best_students_list:
                    for student in best_students_list:
                        print(student)
                else:
                    self.print_message("Empty list")

            elif command == LIST_ALL_DISCIPLINES_WITH_AT_LEAST_ONE_GRADE:
                disciplines_with_at_least_one_grade_list = self.services.disciplines_with_at_least_one_grade()

                if disciplines_with_at_least_one_grade_list:
                    for discipline in disciplines_with_at_least_one_grade_list:
                        print(discipline)
                else:
                    self.print_message("Empty list")

            elif command == DISPLAY_ALL_GRADES_FOR_A_STUDENT:
                id = self.get_id("Input student ID")
                grades_list = self.services.list_all_grades_for_a_student(id)

                if grades_list:
                    for grade in grades_list:
                        print(grade)
                else:
                    self.print_message("Empty list")

            elif command == DISPLAY_ALL_GRADES:
                grades_list = self.services.list_all_grades()

                if grades_list:
                    for grade in grades_list:
                        print(grade)
                else:
                    self.print_message("Empty list")

            elif command == SEARCH_FOR_A_DISCIPLINE:
                BY_ID = 1
                BY_NAME = 2

                print("1. Search by id")
                print("2. Search by name")

                command = self.get_command("Input command --> ")

                if command == BY_ID:
                    id = self.get_id("Input discipline ID --> ")

                    if self.services.search_after_a_discipline_by_id(id):
                        print(self.services.search_after_a_discipline_by_id(id))
                    else:
                        self.display_error("Discipline ID not found")

                elif command == BY_NAME:
                    name = self.get_name("Input discipline name --> ")
                    disciplines_list = self.services.search_after_a_discipline_by_name(name)

                    if disciplines_list:
                        for discipline in disciplines_list:
                            print(discipline)
                    else:
                        self.print_message("Empty list")

                else:
                    self.display_error("Invalid command")

            elif command == EXIT:
                print("Exiting...")
                break
            else:
                self.display_error("Invalide input value! Please retry!")