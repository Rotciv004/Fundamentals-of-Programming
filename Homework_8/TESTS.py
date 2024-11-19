import unittest
from REPOSITORY import School_repository
from SERVICES import Manage_school
from DOMAIN import Student,Discipline,Grade

class Test_Manage_School(unittest.TestCase):
    def setUp(self):
        self.repository = School_repository()
        self.service = Manage_school(self.repository)


    def test_add_student(self):
        self.assertFalse(self.service.add_a_student(Student(1,"Marius")))

    def test_add_discipline(self):
        self.assertFalse(self.service.add_a_discipline(Discipline(1,"Romana")))

    def test_delete_student(self):
        self.assertFalse(self.service.delete_a_student(9999))

    def test_delete_discipline(self):
        self.assertFalse(self.service.delete_a_discipline(9999))

    def test_list_all_students(self):
        student_list = self.service.list_all_students()

        self.assertTrue(len(student_list) > 0)

    def test_update_a_student(self):
        self.assertFalse(self.service.update_a_student(Student(9999,"Marius")))

    def test_search_after_a_student_by_id(self):
        student = self.service.search_after_a_student_by_id(9999)

        self.assertTrue(student is None)

    def test_search_after_a_student_by_name(self):
        student = self.service.search_after_a_student_by_name("qwertyooiucs dgmjj")

        self.assertTrue(len(student) == 0)

    def test_add_a_grade(self):
        self.assertFalse(self.service.add_a_grade(Grade(999,9999,-10)))

    def test_list_all_grades_for_a_student(self):
        self.assertTrue(len(self.service.list_all_grades_for_a_student(999)) == 0)

    def test_list_all_grades(self):
        self.assertTrue(len(self.service.list_all_grades()) != 0)

    def test_list_all_disciplines(self):
        self.assertTrue(len(self.service.list_all_disciplines()) != 0)

    def test_update_a_discipline(self):
        self.assertFalse(self.service.update_a_discipline(Discipline(999,"mate")))

    def test_search_for_a_discipline_by_id(self):
        self.assertTrue(self.service.search_after_a_discipline_by_id(999) is None)

    def test_search_after_a_discipline_by_name(self):
        self.assertTrue(len(self.service.search_after_a_discipline_by_name("amdadqd")) == 0)

    def test_give_a_grade_to_a_student(self):
        self.assertFalse(self.service.give_a_grade_to_a_student(Grade(999,9999,-10)))

    def test_failing_students(self):
        self.assertTrue(len(self.service.failing_students()) != 0)

    def test_best_students(self):
        self.assertTrue(len(self.service.best_students()) != 0)

    def test_disciplines_with_at_least_one_grade(self):
        self.assertTrue(len(self.service.disciplines_with_at_least_one_grade()) > 0)

