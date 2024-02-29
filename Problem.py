import copy

from Action import Action
from State import State
from Mode import Mode


class Problem:
    def __init__(self, initState: State, goal_number: int, mode: Mode):
        self.initState = initState
        self.goal_number = goal_number
        self.mode = mode

    def goal_test(self, state: State) -> bool:  # this method check this state is goal or not
        for i in state.board.gird:
            for j in i:
                if j == self.goal_number:
                    return True
        return False

    def successor(self, state: State) -> list:
        child = []

        child.append(State(copy.deepcopy(state.board), state, state.g_n + 1, 'Action: up'))
        Action.up(child[-1].board, self.mode)

        child.append(State(copy.deepcopy(state.board), state, state.g_n + 1, 'Action: down'))
        Action.down(child[-1].board, self.mode)

        child.append(State(copy.deepcopy(state.board), state, state.g_n + 1, 'Action: left'))
        Action.left(child[-1].board, self.mode)

        child.append(State(copy.deepcopy(state.board), state, state.g_n + 1, 'Action: right'))
        Action.right(child[-1].board, self.mode)

        return child

    @staticmethod
    def print_state(state: State):
        state.board.print_board()

    def set_path_cost(self, cost: list):
        self.path_cost = cost
