from src.DOMAIN import Student

class Ui:
    def __init__(self,services):
        self.services = services

    def error(self,mesage:str):
        print(f"Error: {mesage}")

    def menu(self):
        ADD_A_STUDENT = 1
        DISPLAY_ALL_ASSIGNMENTS = 2
        DISHONESTY_CHECK = 3
        EXIT = 4

        self.services.repository.take_from_file()

        while True:
            print("1. Add a student")
            print("2. Display all assignments")
            print("3. Dishonesty check")
            print("4. Exit")

            command = int(input("Input a command --> "))

            if command == ADD_A_STUDENT:
                id = int(input("Enter student ID: "))
                name = str(input("Enter student name: "))
                solution = str(input("Enter a solution"))

                if self.services.add_a_student(Student(id,name,solution)):
                    print("Student add with succes")
                else:
                    self.error("Invalide input")

            elif command == DISPLAY_ALL_ASSIGNMENTS:
                students_list = self.services.display_all_assignments()

                if students_list:
                    for student in students_list:
                        print(student)
                else:
                    print("No student found")

            elif command == DISHONESTY_CHECK:
                self.services.dishonesty_check()

            elif command == EXIT:
                print("EXIT")
                break
            else:
                print("Invalid command")