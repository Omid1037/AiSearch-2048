# this class only for the first time setup init state for problem and is given to every search
from Board import Board


class State:
    def __init__(self, board: Board, parent, g_n: int, selected_action: str):
        self.board = board
        self.parent = parent
        self.g_n = g_n
        self.selected_action = selected_action

    def __hash__(self):
        return self.board.__hash__()