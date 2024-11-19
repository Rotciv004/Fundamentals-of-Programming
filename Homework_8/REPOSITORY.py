from DOMAIN import Student, Discipline,Grade
import random


class School_repository:

    def __init__(self):
        self.person_name_list =["Ana", "Bogdan", "Cristina", "Daniel", "Elena", "Florin", "Gabriela", "Horia", "Iulia", "John","Katherine", "Lucian", "Maria", "Nicolae", "Olivia", "Paul", "Qamar", "Roxana", "Stefan", "Tatiana", "Ursula", "Victor", "Wanda", "Xander", "Yasmine", "Zoltan"]
        self.discipline_name_list = ["Matematică", "Fizică", "Chimie", "Biologie", "Informatică", "Limba Română", "Limba Engleză",
                 "Istorie", "Geografie", "Educație Fizică", "Muzică", "Arte Plastice", "Economie", "Psihologie",
                 "Filosofie", "Sociologie", "Limba Franceză", "Limba Germană", "Limba Spaniolă", "Programare",
                 "Algebră", "Geometrie", "Literatură", "Fotografie", "Design Grafic"]
        self.students_repository= []
        self.grades_repository= []
        self.disciplines_repository = []

    def generateStudentsRepository(self):
        for i in range(1,21):
            self.students_repository.append(Student(i,random.choice(self.person_name_list)))

    def generateDisciplineRepository(self):
        for i in range(1,21):
            self.disciplines_repository.append(Discipline(i,random.choice(self.discipline_name_list)))

    def generateGradeRepository(self):
        for _ in range(1, 21):
            student_id = random.randint(1, 20)
            subject_id = random.randint(1, 20)
            grade_value = round(random.uniform(1.0, 10.0),2)

            self.grades_repository.append(Grade(student_id, subject_id, grade_value))



    """def __init__(self):
        self.students_repository = [Student(1,"Marius"),Student(2,"Joseph"),Student(3, "Alin"),
                                    Student(4, "Andreea"),Student(5, "Cristina"),Student(6, "Andrei"),
                                    Student(7, "Cristi"),Student(8, "Carlos"),Student(9, "Eric"),
                                    Student(10, "Ionut"),Student(11, "Marian"),Student(12, "Eliza"),
                                    Student(13, "Teodora"),Student(14, "Claudia"),Student(15, "Claudiu"),
                                    Student(16, "Corina"),Student(17, "Relu"),Student(18, "Giorgiana"),
                                    Student(19, "Vancea"),Student(20, "Mery")]

        self.disciplines_repository = [Discipline(1,"Romana"),Discipline(2,"Engleza"),Discipline(3,"Algebra"),
                                       Discipline(4,"Germana"),Discipline(5,"Maghiara"),Discipline(6,"Franceza"),
                                       Discipline(7,"Fizica"),Discipline(8,"Informatica"),Discipline(9,"Religie"),
                                       Discipline(10,"Sport"),Discipline(11,"Biologie"),Discipline(12,"Chimie"),
                                       Discipline(13,"ASC"),Discipline(14,"Dulgherie"),Discipline(15,"FP"),
                                       Discipline(16,"Muzica"),Discipline(17,"Desen"),Discipline(18,"Educatie Tehnologica"),
                                       Discipline(19,"Geometire"),Discipline(20,"Analiza")]

        self.grades_repository = [Grade(1,1,3.30),Grade(2,4,5.30),Grade(3,5,7.30),
                                  Grade(3,4,10.0),Grade(3,6,9.90),Grade(3,7,4.0),
                                  Grade(5,5,8.0),Grade(5,7,3.30),Grade(10,11,3.30),
                                  Grade(13,14,6.30),Grade(12,1,9.30),Grade(2,20,10.0),
                                  Grade(20,1,8.40),Grade(11,19,3.50),Grade(14,14,10.0),
                                  Grade(19,10,4.0),Grade(19,11,5.30),Grade(1,2,9.0),
                                  Grade(20,11,6.75),Grade(2,6,9.30)]"""