class Service:
    def __init__(self,board):
        self.board = board

    def create_the_board(self):

        with open("settings.txt","r") as file:
            datas = file.read()

            datas = datas.split("\n")

            N = int(datas[0])
            apples = int(datas[1])

            board = self.board(N,apples)
            board.put_snake()
            board.generate_apples()

            return board

    def make_a_move(self,board):

        if board.board[board.snake_x][board.snake_y] == "a":
            board.add_a_random_apple()




