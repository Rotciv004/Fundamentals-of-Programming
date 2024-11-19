class Ui:
    def __init__(self,services):
        self.services = services

    def menu(self):
        START = 1
        EXIT = 2

        while True:
            print("1. Start the game")
            print("2. EXIT")

            command = int(input("Input a command --> "))

            if command == START:
                UP = "up"
                RIGHT = "right"
                DOWN = "down"
                LEFT = "left"
                MOVE = "move"

                board = self.services.create_the_board()

                while True:
                    print(board)
                    position = str(input("Input a position --> "))
                    position = position.split(" ")

                    if position[0] == UP:
                        if board.snake_orient == 3:
                                print("Error")
                        else:
                            if board.snake_x != 0:
                                board.board[board.snake_x][board.snake_y] = " "
                                board.snake_x -=1
                                board.snake_orient = 1
                                self.services.make_a_move(board)
                                board.board[board.snake_x][board.snake_y] = "*"
                            else:
                                print("Lose")
                                break

                    elif position[0] == RIGHT:
                        if board.snake_orient == 2:
                                print("Error")
                        else:
                            if board.snake_y != board.N-1:
                                board.board[board.snake_x][board.snake_y] = " "
                                board.snake_y += 1
                                board.snake_orient = 4
                                self.services.make_a_move(board)
                                board.board[board.snake_x][board.snake_y] = "*"
                            else:
                                print("Lose")
                                break

                    elif position[0] == DOWN:
                        if board.snake_orient == 1:
                            print("Error")
                        else:
                            if board.snake_x != board.N-1:
                                board.board[board.snake_x][board.snake_y] = " "
                                board.snake_x += 1
                                board.snake_orient = 3
                                self.services.make_a_move(board)
                                board.board[board.snake_x][board.snake_y] = "*"
                            else:
                                print("Lose")
                                break

                    elif position[0] == LEFT:
                        if board.snake_orient == 4:
                            print("Error")
                        else:
                            if board.snake_x != 0:
                                board.board[board.snake_x][board.snake_y] = " "
                                board.snake_y -= 1
                                board.snake_orient = 2
                                self.services.make_a_move(board)
                                board.board[board.snake_x][board.snake_y] = "*"
                            else:
                                print("Lose")
                                break

                    elif position[0] == MOVE:
                        if len(position) == 2:
                            moves = int(position[1])

                            while moves != 0:
                                if board.snake_orient == 1 and board.snake_x != 0:
                                    board.board[board.snake_x][board.snake_y] = " "
                                    board.snake_x -=1
                                    self.services.make_a_move(board)
                                    board.board[board.snake_x][board.snake_y] = "*"
                                    moves -=1

                                elif board.snake_orient == 2 and board.snake_x != 0:
                                    board.board[board.snake_x][board.snake_y] = " "
                                    board.snake_y -= 1
                                    self.services.make_a_move(board)
                                    board.board[board.snake_x][board.snake_y] = "*"
                                    moves -= 1


                                elif board.snake_orient == 3 and board.snake_x != board.N-1:
                                    board.board[board.snake_x][board.snake_y] = " "
                                    board.snake_x +=1
                                    self.services.make_a_move(board)
                                    board.board[board.snake_x][board.snake_y] = "*"
                                    moves -= 1

                                elif board.snake_orient == 4 and board.snake_x != board.N-1:
                                    board.board[board.snake_x][board.snake_y] = " "
                                    board.snake_y +=1
                                    self.services.make_a_move(board)
                                    board.board[board.snake_x][board.snake_y] = "*"
                                    moves -= 1
                                else:
                                    print("Lose")
                                    break
                            break





            elif command == EXIT:
                print("You exited the game")
                break

            else:
                print("Invalid input please retry!")