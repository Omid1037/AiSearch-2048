# this class only for the first time setup init state for problem and is given to every search
from Board import Board
from Mode import Mode

class State:
    def __init__(self, board: Board, parent, g_n: int, selected_action: str, mode: Mode):
        self.board = board
        self.parent = parent
        self.g_n = g_n
        self.selected_action = selected_action
        self.mode = mode

    def __hash__(self):
        # Convert the board grid to a string representation
        grid_str = ''.join(str(cell) for row in self.board.gird for cell in row)
        # Hash the string representation
        return hash(grid_str)

    def __eq__(self, other):
        # Check equality based on the board configuration
        return self.board.gird == other.board.gird

    def __lt__(self, other):
      # Compare State objects based on their g_n values
      return self.g_n < other.g_n
