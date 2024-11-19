class Student:
    def __init__(self,id:int,name:str):
        self.id = id
        self.name = name

    def get_id(self) -> int:
        return self.id
    def set_id(self,id:int):
        self.id = id

    def get_name(self) -> str:
        return self.name
    def set_name(self,name:str):
        self.name = name

    def __str__(self):
        return (f"ID: {self.id} , Name: {self.name}")

class Discipline:
    def __init__(self,id:int,name:str):
        self.id = id
        self.name = name


    def get_id(self) -> int:
        return self.id
    def set_id(self,id:int):
        self.id = id

    def get_name(self) -> str:
        return self.name
    def set_name(self,name:str):
        self.name = name

    def __str__(self):
        return (f"ID: {self.id} , Name: {self.name}")

class Grade:
    def __init__(self,discipline_id:int,student_id:int,value:float):
        self.discipline_id = discipline_id
        self.student_id = student_id
        self.value = value


    def get_discipline_id(self) -> int:
        return self.discipline_id
    def set_discipline_id(self,discipline_id:int):
        self.discipline_id = discipline_id

    def get_student_id(self) -> int:
        return self.student_id
    def set_student_id(self,student_id:int):
        self.student_id = student_id

    def get_value(self) -> float:
        return self.value
    def set_value(self,value:float):
        self.value = value

    def __str__(self):
        return (f"ID discipline: {self.discipline_id}, ID student: {self.student_id}, GRADE value: {self.value}")
