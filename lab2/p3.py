from collections import deque

class WaterJug:
    def __init__(self, initial_state, goal_state):
        """
        Initialize the water jug problem.
        initial_state: Tuple representing the initial state of the jugs (4L, 3L)
        goal_state: Tuple representing the goal state
        """
        self.initial_state = initial_state
        self.goal_state = goal_state

    def goal_test(self, current_state):
        """
        Check if the current state matches the goal state.
        """
        return current_state == self.goal_state

    def successors(self, state):
        """
        Generate possible states from the current state based on production rules.
        Each state is a tuple (water_in_4L_jug, water_in_3L_jug).
        """
        a, b = state
        successors = []

        # Rule 1: Fill 4L jug
        if a < 4:
            successors.append((4, b))

        # Rule 2: Fill 3L jug
        if b < 3:
            successors.append((a, 3))

        # Rule 3: Empty 4L jug
        if a > 0:
            successors.append((0, b))

        # Rule 4: Empty 3L jug
        if b > 0:
            successors.append((a, 0))

        # Rule 5: Pour water from 4L jug to 3L jug
        if a > 0 and b < 3:
            pour = min(a, 3 - b)
            successors.append((a - pour, b + pour))

        # Rule 6: Pour water from 3L jug to 4L jug
        if b > 0 and a < 4:
            pour = min(b, 4 - a)
            successors.append((a + pour, b - pour))

        return successors

    def bfs(self):
        """
        Perform BFS to find the solution to the water jug problem.
        Returns the path to the solution.
        """
        queue = deque([(self.initial_state, None)])  # (current_state, parent_state)
        closed = {}  # Stores visited states and their parents

        while queue:
            current_state, parent = queue.popleft()
            if current_state in closed:
                continue

            # Mark as visited
            closed[current_state] = parent

            # Check if the goal is reached
            if self.goal_test(current_state):
                return self.generate_path(closed, current_state)

            # Enqueue successors
            for successor in self.successors(current_state):
                if successor not in closed:
                    queue.append((successor, current_state))

        return None  # No solution found

    def dfs(self):
        """
        Perform DFS to find the solution to the water jug problem.
        Returns the path to the solution.
        """
        stack = [(self.initial_state, None)]  # (current_state, parent_state)
        closed = {}  # Stores visited states and their parents

        while stack:
            current_state, parent = stack.pop()
            if current_state in closed:
                continue

            # Mark as visited
            closed[current_state] = parent

            # Check if the goal is reached
            if self.goal_test(current_state):
                return self.generate_path(closed, current_state)

            # Push successors onto the stack
            for successor in self.successors(current_state):
                if successor not in closed:
                    stack.append((successor, current_state))

        return None  # No solution found

    def generate_path(self, closed, state):
        """
        Reconstruct the path from the initial state to the goal state using the CLOSED list.
        """
        path = []
        while state is not None:
            path.append(state)
            state = closed[state]
        path.reverse()
        return path


# Testing the implementation
initial_state = (4, 0)  # 4L jug full, 3L jug empty
goal_state = (2, 0)  # We want exactly 2 liters in the 4L jug

# Create an instance of the WaterJug class
water_jug_problem = WaterJug(initial_state, goal_state)

# Test BFS
print("Solution using BFS:")
bfs_solution = water_jug_problem.bfs()
if bfs_solution:
    print(" -> ".join(map(str, bfs_solution)))
else:
    print("No solution found.")

# Test DFS
print("\nSolution using DFS:")
dfs_solution = water_jug_problem.dfs()
if dfs_solution:
    print(" -> ".join(map(str, dfs_solution)))
else:
    print("No solution found.")
