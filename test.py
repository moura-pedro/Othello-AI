# maze = [[None for _ in range(8)] for j in range(8)]

B = "B"
W = "W"

# maze[3][3] = B
# maze[3][4] = W
# maze[4][3] = W
# maze[4][4] = B


EMPTY = None

def actions(board, player):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if player == board[i][j]:
                possible_actions.update(check_adj(board, i, j, player))


    return possible_actions

def check_adj(board, x, y, player):
    possible_actions = set()

    for i in range(-1, 2):
        for j in range(-1 ,2):
            if i == 0 and j == 0:
                continue
            coords = is_legal(board, x, y, i, j, player)
            if coords is not None:
                possible_actions.add(coords)

    return possible_actions



def is_legal(board, x, y, dx, dy, player):
    i = x + dx
    j = y + dy
    if i < 0 or i >= len(board) or j < 0 or j >= len(board):
        return None

    if player == B:
        opposite = W
    else:
        opposite = B

    while board[i][j] is opposite:
        i = i + dx
        j = j + dy
        if i < 0 or i >= len(board) or j < 0 or j >= len(board):
            return None
        if board[i][j] is EMPTY:
            return (i, j)
    return None
# act = actions(maze, B)

# print(act)