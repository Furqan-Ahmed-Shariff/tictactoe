"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
    ]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for row in board:
        countX += row.count(X)
        countO += row.count(O)

    return X if countO == countX else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)

    if action not in possible_actions:
        raise NameError("Not a Valid action")
    toPlay = player(board)
    new_board = board
    new_board[action[0]][action[1]] = toPlay

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # For every row in the board
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    # For top-left to right diagonal and the first column
    if board[0][0] is not EMPTY:
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][0] == board[1][0] == board[2][0]:
            return board[0][0]

    # For the middle column
    if board[0][1] is not EMPTY and board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]

    # For top-right to left diagonal and the rightmost column
    if board[0][2] is not EMPTY:
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
        if board[0][2] == board[1][2] == board[2][2]:
            return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)
    if win_player is X:
        return 1
    if win_player is O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
