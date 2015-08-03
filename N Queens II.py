# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 12:15:54 2015

@author: ZSHU
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        
        def valid(i,j,board):
            for k in range(i):
                if board[k][j]=='Q':
                    return False 
                if j-(i-k)>=0 and board[k][j-(i-k)]=="Q":
                    return False 
                if j+(i-k)<len(board[k]) and board[k][j+i-k]=="Q":
                    return False 
            return True 
        
        def nqueens(board, level, res):
            if level==n:
                res[0]+=1
                return 
            else: 
                for j in range(n):
                    if valid(level, j, board):
                        vect=['.' for i in range(n)]
                        vect[j]='Q'
                        board[level]=vect
                        nqueens(board, level+1, res)
        res=[0]
        board=[['.' for i in range(n)] for j in range(n)]
        nqueens(board, 0, res)
        return res[0]