"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """

    maze = [[EMPTY for i in range(8)] for j in range(8)]

    maze[3][3] = X
    maze[3][4] = O
    maze[4][3] = O
    maze[4][4] = X
    
    return maze

    # return [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY, X, O, EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY, O, X, EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1

    if countX > countO:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if not actions(board).__contains__(action):
        raise "Not a Valid Action"

    i = action[0]
    j = action[1]

    new_board = deepcopy(board)
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] is not None:
        return board[0][0]
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] is not None:
        return board[1][0]
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] is not None:
        return board[2][0]

    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] is not None:
        return board[0][0]
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] is not None:
        return board[0][1]
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] is not None:
        return board[0][2]

    # Diagonal Checks
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X):
        return True
    elif (winner(board) == O):
        return True

    for i in range(3):
        for j in range(3):
            if  board[i][j] == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
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
