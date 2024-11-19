from REPOSITORY import Text_File_Repo,Binary_File_Repo

class Setings:
    def __init__(self,set_repository:int):
        self.set_repository = set_repository

    def choose_repository(self):
        TEXT_REPOSITORY = 1
        BINARY_REPOSITORY = 2

        if self.set_repository == TEXT_REPOSITORY:
            return Text_File_Repo("students_repo.txt","disiciplines_repo.txt","grades_repo.txt")
        elif self.set_repository == BINARY_REPOSITORY:
            return Binary_File_Repo("students_repo_binary","disiciplines_repo_binary","grades_repo_binary")
        else:
            print("Invalide repository")