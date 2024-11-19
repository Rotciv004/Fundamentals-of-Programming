import texttable
import random

class Board:
    def __init__(self,N:int,apples:int):
        self.N = N
        self.apples = apples
        self.board = [[" " for i in range(self.N)] for j in range(self.N)]
        self.snake_x = self.N // 2
        self.snake_y = self.N // 2
        self.snake_orient = 1
        self.snake_list = []


    def generate_apples(self):
        number_of_apples = 0

        while number_of_apples < self.apples:

            x = random.randint(0,self.N-1)
            y = random.randint(0,self.N-1)

            ADD_VALIDATION = True

            if x == self.snake_x and y == self.snake_y:
                ADD_VALIDATION = False

            for i in self.snake_list:
                if x == i[0] and y == i[1]:
                    ADD_VALIDATION = False

            if self.board[x][y] == "a":
                ADD_VALIDATION = False


            if ADD_VALIDATION:
                self.board[x][y] = "a"
                number_of_apples += 1



    def put_snake(self):
        self.board[self.snake_x][self.snake_y] = "*"

        if self.snake_orient == 1:
            for i in range(0, 2):
                self.board[self.snake_x+i+1][self.snake_y] = "+"
                self.snake_list.append((self.snake_x+i+1,self.snake_y))



    def add_teil(self):

        if self.snake_orient == 1:
            self.snake_list.append((self.snake_list[len(self.snake_list)-1][0]+1,self.snake_list[len(self.snake_list)-1][1]))

        if self.snake_orient == 2:
            self.snake_list.append((self.snake_list[len(self.snake_list)-1][0]+1,self.snake_list[len(self.snake_list)-1][1]))

        if self.snake_orient == 3:
            self.snake_list.append((self.snake_list[len(self.snake_list)-1][0]+1,self.snake_list[len(self.snake_list)-1][1]))

        if self.snake_orient == 4:
            self.snake_list.append((self.snake_list[len(self.snake_list)-1][0]+1,self.snake_list[len(self.snake_list)-1][1]))

    def add_a_random_apple(self):
        number_of_apples = 0

        while number_of_apples < 1:

            x = random.randint(0, self.N - 1)
            y = random.randint(0, self.N - 1)

            ADD_VALIDATION = True

            if x == self.snake_x and y == self.snake_y:
                ADD_VALIDATION = False

            for i in self.snake_list:
                if x == i[0] and y == i[1]:
                    ADD_VALIDATION = False

            if self.board[x][y] == "a":
                ADD_VALIDATION = False



            if ADD_VALIDATION:
                self.board[x][y] = "a"
                number_of_apples += 1

    def __str__(self):
        t = texttable.Texttable()

        header = []

        for i in range(ord('A'), ord('A')+self.N):
            header.append(chr(i))

        header.append("\\")
        t.header(header)

        for i in range(0,self.N):
            t.add_row(self.board[i]+[(i+1)])

        return t.draw()


