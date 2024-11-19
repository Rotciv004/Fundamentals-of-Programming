class Student:
    def __init__(self,id:int,name:str,solution:str):
        """
        Here we have the student class where we construct the studen with a given id, name and solution
        We can get and set id,name and solution at each student
        :param id:
        :param name:
        :param solution:
        """
        self.id = id
        self.name = name
        self.solution = solution

    def __str__(self):
        return(f"{self.id},{self.name},{self.solution}")

    def get_id(self):
        return self.id

    def set_id(self,id:int):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self,name:str):
        self.name = name

    def get_solution(self):
        return self.solution

    def set_solution(self,solution:str):
        self.solution = solution
