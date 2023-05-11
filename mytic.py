#!/bin/python3

import math
import os
import random
import re
import sys

def boardIsFull(board):    
    n, m = len(board), len(board[0])
    for r in range(n):
        for c in range(m):
            if board[r][c] == '_':
                return False
    return True


def boardIsEmpty(board):    
    n, m = len(board), len(board[0])
    for r in range(n):
        for c in range(m):
            if board[r][c] != '_':
                return False
    return True    

def Winner(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '_':
            return 1 if board[row][0] == 'X' else -1
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '_':
            return 1 if board[0][col] == 'X' else -1
    if board[0][0] == board[1][1] == board[2][2]:
        return 1 if board[0][0] == 'X' else 0
    
    if board[0][2] == board[1][1] == board[2][0]:
        return 1 if board[1][1] == 'X' else -1
    
    return 0


def emptySpace(board):
    emptySpaces = []
    for r in range(3):
        for c in range(3):            
            if board[r][c] == '_':
                emptySpaces.append((r, c))
    return emptySpaces


def evalutePosition(board, maximizing):    
    winner = Winner(board)
    if winner == -1: return -1, None
    elif winner == 1: return 1, None
    if boardIsFull(board): return 0, None        
    emptySpaces = emptySpace(board)              
    if maximizing:                    
        retVal = -1
        action = None
        for r, c in emptySpaces:            
            copyOfBoard = board.copy()
            copyOfBoard[r][c] = 'X'
            newEval, newAction = evalutePosition(copyOfBoard, False)
            if newEval > retVal:
                retVal = newEval
                action = (r, c)
        return retVal, action
    elif not maximizing:                  
        retVal = 1
        action = None
        for r, c in emptySpaces:
            copyOfBoard = board.copy()
            copyOfBoard[r][c] = 'O'
            newEval, newAction = evalutePosition(copyOfBoard, True)
            if newEval < retVal:
                retVal = newEval
                action = (r, c)
        return retVal, action
    
        
    
    

def main():        
    t = input()        
    turn = 1 if t == 'X' else 0    
    board = []    
    for _ in range(3):
        line = input()
        board.append(list(line))    
    if boardIsEmpty(board): return 1, 1
    if boardIsFull(board): return 0, 0   
    # ans = [-1]    
    return evalutePosition(board, turn)
    


print(main())
# if __name__ == '__main__':
#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     s = first_multiple_input[1]

'''
X  
___  
___  
_XO
'''

