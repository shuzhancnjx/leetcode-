# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 11:04:13 2015

@author: ZSHU
"""
class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        def valid(i,j,board):
            for k in range(i):
                if board[k][j]=='Q':
                    return False 
                if j-(i-k)>=0 and board[k][j-(i-k)]=="Q":
                    return False 
                if j+(i-k)<len(board[k]) and board[k][j+i-k]=="Q":
                    return False 
            return True 
   
        def nqueen(board,level,res):
            if level==n:
                res.append(["".join(vect) for vect in board])
                return 
            else:
                for j in range(n):
                    if valid(level, j, board):
                        board[level]=['.' for k in range(n)]
                        board[level][j]='Q'
                        nqueen(board, level+1, res)
                 
        board= [['.' for i in range(n)] for j in range(n)]  
        res=[]
        level=0  
        nqueen(board, 0, res )
        return res
        