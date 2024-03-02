"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

B = "B"
W = "W"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """

    maze = [[EMPTY for i in range(8)] for j in range(8)]

    maze[3][3] = B
    maze[3][4] = W
    maze[4][3] = W
    maze[4][4] = B
    # return maze
    

    return [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, W, W, B, W, B, EMPTY, EMPTY],
            [EMPTY, W, W, W, W, B, EMPTY, EMPTY],
            [EMPTY, B, W, EMPTY, W, B, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]
    


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countB = 0
    countW = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == B:
                countB += 1
            elif board[i][j] == W:
                countW += 1

    if countB > countW:
        return W
    return B


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


def result(board, action, player):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    board[i][j] = player
    flipCoins(board, action)

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == B):
        return True
    elif (winner(board) == W):
        return True

    for i in range(3):
        for j in range(3):
            if  board[i][j] == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if B has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == B:
        return 1
    elif winner(board) == W:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == B:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move

def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        temp = min_value(result(board, action))[0]
        if temp > v:
            v = temp
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        temp = max_value(result(board, action))[0]
        if temp < v:
            v = temp
            move = action
            if v == -1:
                return v, move

    return v, move

def flipCoins(board, coord):
    player = board[coord[0]][coord[1]]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            flipsHelper(board, player, coord, i, j)


def flipsHelper(board, player, coord, dx, dy):
    if player == W:
        opposite = B
    else:
        opposite = W
    i = coord[0] + dx
    j = coord[1] + dy
    flips = set()

    if i < 0 or i >= len(board) or j < 0 or j >= len(board):
        return

    while board[i][j] is opposite:
        flips.add((i, j))
        i = i + dx
        j = j + dy

        if i < 0 or i >= len(board) or j < 0 or j >= len(board):
            return
    if board[i][j] is EMPTY:
        return

    for position in flips:
        board[position[0]][position[1]] = player