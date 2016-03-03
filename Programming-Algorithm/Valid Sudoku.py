# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 14:55:37 2015

@author: ZSHU
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        def valid (i,j, board):
            temp, board[i][j]=board[i][j],'.'
            if temp in board[i]:
                return False 
            for k in range(len(board)):
                if board[k][j]==temp:
                    return False 
            for k in range((i/3)*3, (1+i/3)*3):
                if temp in board[k][(j/3)*3:(1+j/3)*3]:
                    return False 
            board[i][j]=temp
            return True 
       
        def sudoku(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]!=".":
                        if not valid(i,j,board):
                            return False 
            return True 
        for i in range(len(board)):
            board[i]=list(board[i])
        return sudoku(board)