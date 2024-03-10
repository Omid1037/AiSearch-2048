from Solution import Solution
from Problem import Problem
from datetime import datetime
from queue import PriorityQueue

class Search:
    @staticmethod
    def bfs(prb: Problem) -> Solution: 
        # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            state = queue.pop(0)
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.goal_test(c):
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None

    @staticmethod
    def dfs(prb: Problem) -> Solution:
        # Implementation of Depth-First Search (DFS)
        start_time = datetime.now()
        stack = []
        visited = set()
        state = prb.initState
        stack.append(state)
        
        while stack:
            state = stack.pop()
            visited.add(state)
            if prb.goal_test(state):
                return Solution(state, prb, start_time)
            neighbors = prb.successor(state)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
        return None

    @staticmethod
    def gbfs(prb: Problem) -> Solution:
        # Implementation of Greedy Best-First Search (GBFS)
        start_time = datetime.now()
        queue = PriorityQueue()
        visited = set()
        state = prb.initState
        queue.put((0, state))
        
        while not queue.empty():
            _, state = queue.get()
            visited.add(state)
            if prb.goal_test(state):
                return Solution(state, prb, start_time)
            neighbors = prb.successor(state)
            for neighbor in neighbors:
                if neighbor not in visited:
                    priority = Search.heuristic_function(neighbor)
                    queue.put((priority, neighbor))
        return None

    @staticmethod
    def heuristic_function(state: State) -> int:
        max_tile = max(max(row) for row in state.board.gird)
        return max_tile  # Return the value of the maximum tile
