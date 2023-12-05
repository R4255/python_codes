class State:
    def __init__(self, missionaries, cannibals, boat):# parametrized constructor
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
    def is_valid(self): #to check if the state is valid or not
        #keeping in mind that cannibals don't exceed missionaries
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        return (self.missionaries >= self.cannibals or self.missionaries == 0) and \
               (3 - self.missionaries >= 3 - self.cannibals or 3 - self.missionaries == 0)
    def is_goal(self): #to check whether we have reached the goal state or not
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0
    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat
    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))
def dfs(current_state, visited, path):#depth first search approach
    if current_state.is_goal():
        return path
    visited.add(current_state)#if it is not the goal_state add that current state to the visited set
    for action in actions:
        new_state = perform_action(current_state, action)
        if new_state.is_valid() and new_state not in visited:
            result = dfs(new_state, visited, path + [new_state])
            if result is not None:
                return result
    return None
def perform_action(state, action):
    missionaries, cannibals, boat = state.missionaries, state.cannibals, state.boat
    if action == "MM":
        return State(missionaries - 2, cannibals, 1 - boat)
    elif action == "CC":
        return State(missionaries, cannibals - 2, 1 - boat)
    elif action == "MC":
        return State(missionaries - 1, cannibals - 1, 1 - boat)
    elif action == "M":
        return State(missionaries - 1, cannibals, 1 - boat)
    elif action == "C":
        return State(missionaries, cannibals - 1, 1 - boat)
def print_solution(path):
    for i, state in enumerate(path):
        print(f"Step {i}: {state.missionaries}M-{state.cannibals}C-{state.boat}B")
# Define the initial state and possible actions
initial_state = State(3, 3, 1)
actions = ["MM", "CC", "MC", "M", "C"]
# Solve the problem using DFS
visited = set()
path = dfs(initial_state, visited, [initial_state])
# Print the solution
if path is not None:
    print("Solution found:")
    print_solution(path)
else:
    print("No solution found.")