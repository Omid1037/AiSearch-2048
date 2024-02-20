from Board import Board


class Action:

    @staticmethod
    def left(board: Board):
        for i in range(board.height - 1):
            for j in range(board.width):
                board.gird[j][i] += board.gird[j][i + 1]
                board.gird[j][i + 1] = 0

    @staticmethod
    def right(board: Board):
        for i in range(board.height - 1, 0, -1):
            for j in range(board.width):
                board.gird[j][i] += board.gird[j][i - 1]
                board.gird[j][i - 1] = 0

    @staticmethod
    def down(board: Board):
        for i in range(board.width - 1, 0, -1):
            for j in range(board.height):
                board.gird[i][j] += board.gird[i - 1][j]
                board.gird[i - 1][j] = 0

    @staticmethod
    def up(board: Board):
        for i in range(board.width - 1):
            for j in range(board.height - 1):
                board.gird[i][j] += board.gird[i + 1][j]
                board.gird[i + 1][j] = 0
