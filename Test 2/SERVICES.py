from src.DOMAIN import Student


class Services:
    def __init__(self,repository):
        self.repository = repository

    def add_a_student(self,student:Student)-> bool:
        """
        Here we have function witch hellp us to stor a student into the repository. After all verifications we succesfuly can add a student
        :param student: Here we get a student from console
        :return:
        """

        self.repository.take_from_file()

        for stud in self.repository.students_repository:
            if student.get_id() == stud.get_id():
                return False

        if len(student.get_name()) < 3:
            return False

        if len(student.get_solution()) == 0:
            return False

        self.repository.students_repository.append(student)

        self.repository.put_in_file()

        return True

    def display_all_assignments(self):
        """
        Here we get the all assignements from repository and show it in UI
        :return:
        """
        self.repository.take_from_file()

        return self.repository.students_repository

    def dishonesty_check(self):
        """
        Here we have the function witch calculate de dishonesty check for each student from the repository
        :return: Students witch
        """

        self.repository.take_from_file()

        for first_student in self.repository.students_repository:
            dishonesty_check_list = []
            percent_list = []

            for second_student in self.repository.students_repository:
                if first_student.get_id() != second_student.get_id():

                    solution_parts = second_student.get_solution().split(" ")
                    len_second_student_solution = len(solution_parts)
                    words_contor = 0

                    for solution_part in solution_parts:
                        if solution_part in first_student.get_solution():
                            words_contor += 1

                    percent = words_contor * 100 / len_second_student_solution

                    if percent >= 20.0:
                        dishonesty_check_list.append(second_student)
                        percent_list.append(percent)

            if dishonesty_check_list and percent_list:
                print(f"For {first_student.get_name} -> ")

                for index in range(0, len(dishonesty_check_list)):
                    print(f"{dishonesty_check_list[index].name} {percent_list[index]}%")







