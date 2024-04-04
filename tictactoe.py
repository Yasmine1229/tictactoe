"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    global currentPlayer 
    currentPlayer=False
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount= oCount = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==X:
                xCount+=1
            elif board[i][j]==O:
                oCount +=1
    print(xCount,oCount)
    return X if oCount == xCount else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    Actions=set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==EMPTY:
                Actions.add((i,j))
    
    return Actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j=action
    newBoard=copy.deepcopy(board)
    if action not in actions(board) :
        raise "InvalidActionException"
    
    newBoard[i][j]=player(board)
    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if(board[i][0]==board[i][1]==board[i][2] and board[i][0] is not EMPTY):
            return board[i][0]
        elif board[0][i]==board[1][i]==board[2][i] and board[0][i] is not EMPTY :
            return board[0][i]
        
    if (board[1][1] is not EMPTY) and ((board[0][0]==board[1][1]==board[2][2]) or (board[0][2] == board[1][1] == board[2][0])) :
        return board[1][1]
    
    
    
    return None
    
def isTie(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] is EMPTY:
                return False
    return True

def terminal(board):
    if(winner(board)==X or winner(board)==O or isTie(board)):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    play=player(board)
    if(terminal(board)):
        return None
    elif play==X:
        lst=[]
        for action in actions(board):
            lst.append([MinValue(result(board,action)),action])
        return sorted(lst,key=lambda x: x[0],reverse=True)[0][1]
    elif play==O:
        lst=[]
        for action in actions(board):
            lst.append([MaxValue(result(board,action)),action])
        return sorted(lst,key=lambda x: x[0])[0][1]


    
def MaxValue(board):
    if terminal(board):
        return utility(board)
    v=-math.inf
    for action in actions(board):
        v=max(v,MinValue(result(board,action)))
    return v

def MinValue(board):
    if(terminal(board)):
        return utility(board)
    v=math.inf
    for action in actions(board):
        v=min(v,MaxValue(result(board,action)))
    return v