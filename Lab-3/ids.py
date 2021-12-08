# Iterative Deepening Search in search of target - Using Recursion

def dfs(src, target, limit, visited_states):
    # Base case if Target found
    if src == target:
        return True

    # Base case if limit exceeded
    if (limit <= 0):
        return False

        # Add source to visited_states
    visited_states.append(src);

    # Find possible slides up, down, left right to current empty site
    ### Jump to possible_moves function
    poss_moves = possible_moves(src, visited_states)

    # For all possible moves gotten from the possible moves function
    # Check if src equals to new targets
    # Return True if target found in given depth limit
    for move in poss_moves:
        if dfs(move, target, limit - 1, visited_states): return True
    return False


def possible_moves(state, visited_states):
    # Find index of empty spot and assign it to b
    b = state.index(-1);

    # 'd' for down, 'u' for up, 'r' for right, 'l' for left - directions array
    d = []

    # Add all possible direction into directions array - Hint using if statements
    if b - 3 in range(9):
        d.append('u')
    if b not in [0, 3, 6]:
        d.append('l')
    if b not in [2, 5, 8]:
        d.append('r')
    if b + 3 in range(9):
        d.append('d')

    # If direction is possible then add state to move
    pos_moves = []

    # for all possible directions find the state if that move is played
    ### Jump to gen function to generate all possible moves in the given directions
    for m in d:
        pos_moves.append(gen(state, m, b))

    # return all possible moves only if the move not in visited_states
    return [move for move in pos_moves if move not in visited_states]


def gen(state, m, b):  # m(move) is direction to slide, b(blank) is index of empty spot
    # create a copy of current state to test the move
    temp = state.copy()

    # if move is to slide empty spot to the left and so on
    if m == 'u': temp[b - 3], temp[b] = temp[b], temp[b - 3]
    if m == 'l': temp[b - 1], temp[b] = temp[b], temp[b - 1]
    if m == 'r': temp[b + 1], temp[b] = temp[b], temp[b + 1]
    if m == 'd': temp[b + 3], temp[b] = temp[b], temp[b + 3]

    # return new state with tested move to later check if "src == target"
    return temp

def iddfs(src,target,depth):
    visited_states = []
    # Return Min depth at which the target was found
    for i in range(1, depth+1):
        if dfs(src, target, i, visited_states): return i
    return -1

# src = [1,2,3,-1,4,5,6,7,8]
# target=[1,2,3,6,4,5,-1,7,8]
src = [1,2,3,-1,4,5,6,7,8]
target=[1,2,3,4,5,-1,6,7,8]
depth = 25
val = iddfs(src,target,depth)
if val != -1:
    print(val,True)
else:
    print(False)
    
    
--------------------------------------------------------------------------------------------------------------------------------------------------

C:\Users\bmsce\Lab3\venv\Scripts\python.exe C:/Users/bmsce/Lab3/lab3.py
2 True

Process finished with exit code 0
